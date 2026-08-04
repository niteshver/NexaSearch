"""
Test suite for NexaSearch production improvements.

Tests cover:
- Pydantic validation
- Bloom filter deduplication
- Circuit breaker state transitions
- Retry strategies
- URL canonicalization
- Async semaphore concurrency
- Checkpoint persistence
"""

import pytest
import asyncio
from pathlib import Path
import tempfile
import json

from src.seeder.sources import (
    SeedingSource,
    URLNormalizer,
    PatternMatcher,
    SourcePriority,
)
from src.seeder.url_seeder import (
    URLSeeder,
    URLSeederConfig,
    CircuitBreaker,
    CircuitBreakerConfig,
    RetryConfig,
    RetryStrategy,
    BloomFilter,
    CorrelatedLogger,
)


# ============================================================================
# Pydantic Validation Tests
# ============================================================================

class TestSeededSourceValidation:
    """Test Pydantic SeedingSource validation."""
    
    def test_valid_config(self):
        """Valid config passes validation."""
        source = SeedingSource(
            domain="pypi.org",
            source="sitemap",
            pattern="*/project/*",
            max_urls=5000,
            use_bm25=False,
        )
        assert source.domain == "pypi.org"
        assert source.max_urls == 5000
    
    def test_invalid_max_urls(self):
        """max_urls validation."""
        with pytest.raises(ValueError):
            SeedingSource(domain="test", max_urls=200000)  # > 100000
    
    def test_invalid_concurrency(self):
        """concurrency validation."""
        with pytest.raises(ValueError):
            SeedingSource(domain="test", concurrency=100)  # > 50
    
    def test_bm25_requires_query(self):
        """BM25 enabled without query fails."""
        with pytest.raises(ValueError):
            SeedingSource(domain="test", use_bm25=True, query=None)


# ============================================================================
# URL Canonicalization Tests
# ============================================================================

class TestURLNormalizer:
    """Test URL normalization and canonicalization."""
    
    def test_canonicalize_basic(self):
        """Basic URL canonicalization."""
        url = "https://example.com/path"
        canonical = URLNormalizer.canonicalize(url)
        assert canonical == "https://example.com/path"
    
    def test_canonicalize_strip_fragment(self):
        """Remove fragment (#)."""
        url = "https://example.com/path#section"
        canonical = URLNormalizer.canonicalize(url)
        assert "#section" not in canonical
        assert "section" not in canonical
    
    def test_canonicalize_lowercase_domain(self):
        """Lowercase domain."""
        url = "https://EXAMPLE.COM/path"
        canonical = URLNormalizer.canonicalize(url)
        assert "example.com" in canonical
        assert "EXAMPLE.COM" not in canonical
    
    def test_canonicalize_sort_params(self):
        """Sort query parameters."""
        url = "https://example.com?z=1&a=2&m=3"
        canonical = URLNormalizer.canonicalize(url)
        # Should be ordered: a, m, z
        a_pos = canonical.find("a=2")
        m_pos = canonical.find("m=3")
        z_pos = canonical.find("z=1")
        assert a_pos < m_pos < z_pos
    
    def test_is_nonsense_url_tracking(self):
        """Detect tracking URLs."""
        assert URLNormalizer.is_nonsense_url("https://example.com?utm_source=x")
        assert URLNormalizer.is_nonsense_url("https://example.com?ga_id=y")
    
    def test_is_nonsense_url_clean(self):
        """Whitelist clean URLs."""
        assert not URLNormalizer.is_nonsense_url("https://example.com/docs/api")


# ============================================================================
# Bloom Filter Tests
# ============================================================================

class TestBloomFilter:
    """Test Bloom filter deduplication."""
    
    def test_bloom_filter_add_contains(self):
        """Add and contains operations."""
        bf = BloomFilter(expected_elements=100)
        bf.add("https://example.com")
        assert bf.contains("https://example.com")
    
    def test_bloom_filter_false_negative(self):
        """No false negatives (must contain added items)."""
        bf = BloomFilter(expected_elements=100)
        urls = ["https://example1.com", "https://example2.com"]
        for url in urls:
            bf.add(url)
        
        for url in urls:
            assert bf.contains(url), f"False negative for {url}"
    
    def test_bloom_filter_memory_usage(self):
        """Memory usage is reasonable."""
        bf = BloomFilter(expected_elements=1_000_000)
        memory_mb = bf.memory_usage_mb()
        # Should be ~50 MB for 1M elements
        assert memory_mb < 100, f"Memory usage too high: {memory_mb} MB"


# ============================================================================
# Circuit Breaker Tests
# ============================================================================

class TestCircuitBreaker:
    """Test circuit breaker state transitions."""
    
    def test_closed_state_normal(self):
        """CLOSED state allows requests."""
        cb = CircuitBreaker()
        assert cb.can_attempt()
        assert cb.state.value == "closed"
    
    def test_open_on_failure_threshold(self):
        """OPEN after failure threshold."""
        config = CircuitBreakerConfig(failure_threshold=3)
        cb = CircuitBreaker(config=config)
        
        for _ in range(3):
            cb.record_failure()
        
        assert cb.state.value == "open"
        assert not cb.can_attempt()
    
    def test_half_open_after_timeout(self):
        """HALF_OPEN after recovery timeout."""
        import time
        config = CircuitBreakerConfig(failure_threshold=1, recovery_timeout=0.1)
        cb = CircuitBreaker(config=config)
        
        cb.record_failure()
        assert cb.state.value == "open"
        assert not cb.can_attempt()
        
        time.sleep(0.2)
        assert cb.can_attempt()
        assert cb.state.value == "half_open"
    
    def test_recover_from_half_open(self):
        """CLOSED after successes in HALF_OPEN."""
        config = CircuitBreakerConfig(failure_threshold=1, success_threshold=2)
        cb = CircuitBreaker(config=config)
        
        cb.record_failure()
        assert cb.state.value == "open"
        
        import time
        time.sleep(0.1)  # Wait for recovery
        
        cb.record_success()
        assert cb.state.value == "half_open"
        
        cb.record_success()
        assert cb.state.value == "closed"


# ============================================================================
# Retry Strategy Tests
# ============================================================================

class TestRetryStrategy:
    """Test retry delay calculations."""
    
    def test_exponential_backoff(self):
        """Exponential backoff: 2^attempt."""
        config = RetryConfig(
            base_delay=1.0,
            strategy=RetryStrategy.EXPONENTIAL,
            jitter=False,
        )
        assert config.get_delay(0) == 1.0  # 2^0 = 1
        assert config.get_delay(1) == 2.0  # 2^1 = 2
        assert config.get_delay(2) == 4.0  # 2^2 = 4
    
    def test_linear_backoff(self):
        """Linear backoff: attempt * base_delay."""
        config = RetryConfig(
            base_delay=1.0,
            strategy=RetryStrategy.LINEAR,
            jitter=False,
        )
        assert config.get_delay(1) == 1.0
        assert config.get_delay(2) == 2.0
        assert config.get_delay(3) == 3.0
    
    def test_max_delay_capped(self):
        """Max delay enforced."""
        config = RetryConfig(
            base_delay=1.0,
            max_delay=10.0,
            strategy=RetryStrategy.EXPONENTIAL,
            jitter=False,
        )
        # 2^10 = 1024, but capped at 10
        assert config.get_delay(10) == 10.0
    
    def test_jitter_within_range(self):
        """Jitter adds randomness."""
        config = RetryConfig(
            base_delay=10.0,
            strategy=RetryStrategy.EXPONENTIAL,
            jitter=True,
        )
        delays = [config.get_delay(2) for _ in range(100)]
        # Should be around 4.0 ± 10%
        assert all(3.6 < d < 4.4 for d in delays)


# ============================================================================
# Pattern Matcher Tests
# ============================================================================

class TestPatternMatcher:
    """Test pattern matching."""
    
    def test_wildcard_matches_all(self):
        """* pattern matches all URLs."""
        matcher = PatternMatcher()
        assert matcher.matches("https://example.com", "*")
        assert matcher.matches("https://example.com/deep/path", "*")
    
    def test_path_pattern_matching(self):
        """Path patterns work."""
        matcher = PatternMatcher()
        assert matcher.matches("https://github.com/user/repo/blob/main/file.py", "*/blob/*")
        assert not matcher.matches("https://github.com/user/repo/tree/main", "*/blob/*")
    
    def test_pattern_caching(self):
        """Patterns are cached."""
        matcher = PatternMatcher()
        pattern1 = matcher.compile_pattern("*/docs/*")
        pattern2 = matcher.compile_pattern("*/docs/*")
        assert pattern1 is pattern2  # Same cached object


# ============================================================================
# Async Semaphore Tests
# ============================================================================

class TestAsyncSemaphore:
    """Test concurrent request limiting."""
    
    @pytest.mark.asyncio
    async def test_semaphore_limits_concurrency(self):
        """Semaphore enforces max concurrent requests."""
        sem = asyncio.Semaphore(2)
        active = 0
        max_active = 0
        
        async def task():
            nonlocal active, max_active
            async with sem:
                active += 1
                max_active = max(max_active, active)
                await asyncio.sleep(0.1)
                active -= 1
        
        await asyncio.gather(*[task() for _ in range(10)])
        
        # Max concurrent should be 2
        assert max_active == 2


# ============================================================================
# Checkpoint Tests
# ============================================================================

class TestCheckpointing:
    """Test checkpoint persistence."""
    
    def test_checkpoint_save_load(self):
        """Save and load checkpoint."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = URLSeederConfig(output_dir=tmpdir)
            
            # Save checkpoint
            completed = ["seeding", "crawling"]
            config.checkpoint_file.write_text(json.dumps({
                "completed_stages": completed,
                "timestamp": "2024-01-01T00:00:00",
            }))
            
            # Load checkpoint
            with open(config.checkpoint_file) as f:
                checkpoint = json.load(f)
            
            assert checkpoint["completed_stages"] == completed


# ============================================================================
# Integration Tests
# ============================================================================

class TestURLSeederIntegration:
    """Integration tests for URL seeder."""
    
    @pytest.mark.asyncio
    async def test_seeder_initialization(self):
        """Seeder initializes correctly."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config = URLSeederConfig(output_dir=tmpdir)
            seeder = URLSeeder(config=config)
            
            assert seeder.correlation_id
            assert seeder.semaphores
            assert seeder.circuit_breakers
            assert seeder.metrics


# ============================================================================
# Performance Tests
# ============================================================================

class TestPerformance:
    """Performance benchmarks."""
    
    def test_url_canonicalization_speed(self):
        """URL canonicalization is fast (<1ms)."""
        import time
        
        url = "https://EXAMPLE.COM/path?z=1&a=2#fragment"
        
        start = time.time()
        for _ in range(1000):
            URLNormalizer.canonicalize(url)
        elapsed = time.time() - start
        
        # Should be fast
        assert elapsed < 0.1  # <0.1ms per call on average
    
    def test_bloom_filter_lookup_speed(self):
        """Bloom filter lookups are fast."""
        import time
        
        bf = BloomFilter(expected_elements=100000)
        for i in range(10000):
            bf.add(f"url_{i}")
        
        start = time.time()
        for i in range(100000):
            bf.contains(f"url_{i % 10000}")
        elapsed = time.time() - start
        
        # Should be fast
        assert elapsed < 0.01  # <0.1µs per lookup


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
