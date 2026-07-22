import pytest

from src.chunking.chunker import DocumentChunker


def test_chunker_rejects_non_advancing_overlap():
    with pytest.raises(ValueError, match="chunk_overlap"):
        DocumentChunker(chunk_size=10, chunk_overlap=10)
