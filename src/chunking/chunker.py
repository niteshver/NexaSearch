import hashlib
from typing import List, Dict, Any
from src.config.settings import settings

class DocumentChunker:
    def __init__(self, chunk_size: int = None, chunk_overlap: int = None):
        self.chunk_size = chunk_size or settings.CHUNK_SIZE
        self.chunk_overlap = chunk_overlap or settings.CHUNK_OVERLAP

    def chunk_document(self, doc: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Split a single document into section-aware chunks.
        """
        url = doc.get("url", "")
        title = doc.get("title", "") or "Untitled Page"
        text = doc.get("text", "") or doc.get("markdown", "")
        doc_id = doc.get("id") or hashlib.md5(url.encode()).hexdigest()
        doc_metadata = doc.get("metadata", {})

        if not text:
            return []

        chunks = []
        lines = text.splitlines()
        
        current_heading = "Introduction"
        current_section_lines = []
        
        # Parse document by headings
        sections = []  # List of tuples (heading, section_text)
        
        for line in lines:
            # Check if line is a header
            header_match = re.match(r'^(#{1,6})\s+(.+)$', line.strip())
            if header_match:
                # Save previous section if it has content
                if current_section_lines:
                    sections.append((current_heading, "\n".join(current_section_lines)))
                    current_section_lines = []
                # Update current heading
                current_heading = header_match.group(2).strip()
            else:
                current_section_lines.append(line)
        
        # Add final section
        if current_section_lines:
            sections.append((current_heading, "\n".join(current_section_lines)))

        # If no sections were extracted (no markdown headers), process the entire text as one section
        if not sections:
            sections.append(("Content", text))

        # Now chunk each section based on chunk size and overlap
        chunk_idx = 0
        for heading, sec_text in sections:
            sec_words = sec_text.split()
            if not sec_words:
                continue

            # If section is small enough, make it a single chunk
            if len(sec_words) <= self.chunk_size:
                chunk_text = " ".join(sec_words)
                chunks.append(self._create_chunk_dict(
                    doc_id, chunk_idx, chunk_text, heading, url, title, doc_metadata
                ))
                chunk_idx += 1
            else:
                # Section is too large; split with overlap
                i = 0
                while i < len(sec_words):
                    # Extract slice of words
                    chunk_word_slice = sec_words[i : i + self.chunk_size]
                    chunk_text = " ".join(chunk_word_slice)
                    
                    chunks.append(self._create_chunk_dict(
                        doc_id, chunk_idx, chunk_text, heading, url, title, doc_metadata
                    ))
                    chunk_idx += 1
                    
                    # Advance by step size (chunk_size - overlap)
                    i += (self.chunk_size - self.chunk_overlap)
                    if i >= len(sec_words) - self.chunk_overlap and i < len(sec_words):
                        # Avoid creating a tiny final chunk by breaking early if remaining words is small
                        # Instead, let's keep it if there is enough content
                        last_slice = sec_words[i:]
                        if len(last_slice) > 30:  # Only write final chunk if > 30 words
                            chunks.append(self._create_chunk_dict(
                                doc_id, chunk_idx, " ".join(last_slice), heading, url, title, doc_metadata
                            ))
                        break

        return chunks

    def _create_chunk_dict(self, doc_id: str, index: int, text: str, heading: str, url: str, title: str, doc_metadata: dict) -> Dict[str, Any]:
        """Helper to structure chunk dictionary."""
        chunk_id = f"{doc_id}_c{index}"
        words = text.split()
        return {
            "chunk_id": chunk_id,
            "doc_id": doc_id,
            "text": text,
            "heading": heading,
            "url": url,
            "title": title,
            "word_count": len(words),
            "metadata": {
                **doc_metadata,
                "chunk_index": index,
                "heading": heading
            }
        }

    def chunk_batch(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Split a batch of documents into chunks.
        """
        all_chunks = []
        for doc in documents:
            all_chunks.extend(self.chunk_document(doc))
        return all_chunks

import re
