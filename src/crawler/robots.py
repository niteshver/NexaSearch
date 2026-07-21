import urllib.robotparser
from urllib.parse import urlparse
import aiohttp
import asyncio
from src.crawler.logger import logger
from src.config.settings import settings

class RobotsParser:
    def __init__(self, user_agent: str = None):
        self.user_agent = user_agent or settings.CRAWL_USER_AGENT
        self._cache = {}
        self._lock = asyncio.Lock()

    async def is_allowed(self, url: str) -> bool:
        """
        Check if a URL is allowed to be crawled according to its domain's robots.txt.
        """
        parsed = urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            return False

        domain = f"{parsed.scheme}://{parsed.netloc}"
        
        async with self._lock:
            if domain not in self._cache:
                self._cache[domain] = await self._fetch_robots_txt(domain)
        
        rp = self._cache[domain]
        if rp is None:
            # If robots.txt could not be fetched or parsed, assume allowed
            return True
            
        try:
            return rp.can_fetch(self.user_agent, url)
        except Exception as e:
            logger.error(f"Error checking robots.txt for {url}: {e}")
            return True

    async def _fetch_robots_txt(self, domain: str) -> urllib.robotparser.RobotFileParser:
        """
        Fetch and parse robots.txt for a domain asynchronously.
        """
        robots_url = f"{domain}/robots.txt"
        rp = urllib.robotparser.RobotFileParser()
        try:
            async with aiohttp.ClientSession(headers={"User-Agent": self.user_agent}) as session:
                async with session.get(robots_url, timeout=10) as response:
                    if response.status == 200:
                        content = await response.text()
                        rp.parse(content.splitlines())
                        return rp
                    elif response.status == 404:
                        # 404 means no crawl restrictions
                        return None
        except Exception as e:
            logger.warning(f"Could not fetch robots.txt for {domain}: {e}. Defaulting to allowed.")
        
        return None
