from src.processing.deduplication import DeduplicationPipeline

def test_exact_deduplication():
    pipeline = DeduplicationPipeline()
    doc1_text = "This is a unique page with some specific content."
    doc2_text = "This is a unique page with some specific content."  # exact duplicate text
    
    # First page is not a duplicate
    assert pipeline.is_exact_duplicate(doc1_text, "https://example.com/page1") is False
    pipeline.add_exact_hash(doc1_text, "https://example.com/page1")
    
    # Second page with same content is duplicate
    assert pipeline.is_exact_duplicate(doc2_text, "https://example.com/page2") is True
    
    # Same URL is duplicate
    assert pipeline.is_exact_duplicate("Different text.", "https://example.com/page1") is True

def test_near_deduplication():
    pipeline = DeduplicationPipeline(jaccard_threshold=0.8)
    
    doc1_text = "This is a very long text to check near duplicate detection shingles. We will run LSH and MinHash algorithms."
    # Modify slightly
    doc2_text = "This is a very long text to check near duplicate detection shingles. We will run LSH and MinHash algorithm."
    # Different text
    doc3_text = "Completely different content about python programming and semantic search engines."

    # First doc
    assert pipeline.is_near_duplicate("doc1", doc1_text) is False
    
    # Second doc (near duplicate, should trigger True)
    assert pipeline.is_near_duplicate("doc2", doc2_text) is True
    
    # Third doc (different, should trigger False)
    assert pipeline.is_near_duplicate("doc3", doc3_text) is False
