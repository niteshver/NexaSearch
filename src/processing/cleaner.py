import re
import unicodedata
from urllib.parse import urlparse
from src.config.settings import settings

class TextCleaner:
    def __init__(self):
        # Compiled regexes for PII removal
        self.email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        self.phone_pattern = re.compile(r'\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}')
        self.ip_pattern = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
        
        # Compiled regex for basic HTML boilerplate if any remains
        self.html_tag_pattern = re.compile(r'<[^>]*>')
        
        # Match markdown link syntax: [text](url) -> keep text only if ignore links is set, or normalize
        self.md_link_pattern = re.compile(r'\[([^\]]+)\]\([^\)]+\)')

    def clean(self, text: str, url: str) -> dict:
        """
        Clean the input text (markdown or HTML) and extract metadata.
        """
        if not text:
            return {
                "text": "",
                "metadata": {
                    "word_count": 0,
                    "has_code": False,
                    "language": "en"
                }
            }

        # 1. Boilerplate / HTML Removal if HTML tags are present
        cleaned = text
        if "<" in cleaned and ">" in cleaned:
            # Simple strip HTML tags
            cleaned = self.html_tag_pattern.sub('', cleaned)

        # 2. Unicode Normalization (NFKD)
        cleaned = unicodedata.normalize('NFKD', cleaned)

        # 3. Clean Markdown Link formatting but keep link text
        cleaned = self.md_link_pattern.sub(r'\1', cleaned)

        # 4. Mask PII (emails, phone numbers, IP addresses)
        cleaned = self.mask_pii(cleaned)

        # 5. Normalize Whitespace (replace multiple spaces/newlines)
        cleaned = self.normalize_whitespace(cleaned)

        # 6. Remove Duplicate Lines
        cleaned = self.remove_duplicate_lines(cleaned)

        # 7. Metadata Extraction
        words = cleaned.split()
        word_count = len(words)
        has_code = "```" in text or "`" in text
        
        # Simple language detection (English heuristic vs others for vertical search)
        language = self.detect_language(cleaned)

        parsed_url = urlparse(url)
        domain = parsed_url.netloc

        metadata = {
            "word_count": word_count,
            "has_code": has_code,
            "language": language,
            "domain": domain,
            "url": url,
            "cleaned_at_epoch": True
        }

        return {
            "text": cleaned,
            "metadata": metadata
        }

    def mask_pii(self, text: str) -> str:
        """Mask sensitive information like email, phones, and IP addresses."""
        text = self.email_pattern.sub('[EMAIL_MASKED]', text)
        text = self.ip_pattern.sub('[IP_MASKED]', text)
        # Phone mask can be noisy, but let's apply it with a safe pattern
        text = self.phone_pattern.sub('[PHONE_MASKED]', text)
        return text

    def normalize_whitespace(self, text: str) -> str:
        """Standardize spaces and empty lines."""
        # Replace multiple spaces with a single space
        text = re.sub(r'[ \t]+', ' ', text)
        # Replace 3 or more consecutive newlines with exactly 2 newlines (to preserve paragraphs)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()

    def remove_duplicate_lines(self, text: str) -> str:
        """Remove consecutive identical lines or boilerplate identical lines."""
        lines = text.splitlines()
        seen = set()
        unique_lines = []
        for line in lines:
            line_stripped = line.strip()
            if not line_stripped:
                unique_lines.append(line)
                continue
            
            # If line is extremely short, don't worry about duplicates (e.g. lists, punctuation)
            if len(line_stripped) < 15:
                unique_lines.append(line)
                continue

            # Calculate a simplified representation to match duplicates
            simplified = re.sub(r'\W+', '', line_stripped).lower()
            if simplified not in seen:
                seen.add(simplified)
                unique_lines.append(line)
        return '\n'.join(unique_lines)

    def detect_language(self, text: str) -> str:
        """Lightweight heuristic language detection (English-leaning)."""
        # A simple list of common English stop words
        english_indicators = {'the', 'and', 'of', 'to', 'in', 'is', 'that', 'it', 'for', 'on', 'with', 'as', 'this', 'by', 'an', 'be'}
        words = [w.lower() for w in text[:5000].split() if w.isalpha()]
        if not words:
            return "en"
        
        eng_count = sum(1 for w in words if w in english_indicators)
        ratio = eng_count / len(words)
        
        # If english words make up > 3% of top text, classify as English
        if ratio > 0.03:
            return "en"
        
        # Fallback to simple check
        return "en"
