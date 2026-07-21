import pytest
import os
import shutil
from src.search.bm25_index import BM25Index
from src.search.engine import SearchEngine

@pytest.fixture
def temp_index_dir():
    dir_path = "data/test_index"
    os.makedirs(dir_path, exist_ok=True)
    yield dir_path
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)

def test_bm25_indexing(temp_index_dir):
    index = BM25Index()
    
    chunks = [
        {"chunk_id": "c1", "text": "Python programming language is awesome.", "title": "Python page", "url": "url1", "heading": "Intro"},
        {"chunk_id": "c2", "text": "Deep learning models are built using neural networks.", "title": "ML page", "url": "url2", "heading": "ML Intro"},
        {"chunk_id": "c3", "text": "How to compile code and run tests.", "title": "Dev page", "url": "url3", "heading": "Coding"},
    ]
    
    index.index_documents(chunks)
    
    # Test search matching
    res = index.search("programming language")
    assert len(res) > 0
    assert res[0][0]["chunk_id"] == "c1"
    
    res_ml = index.search("neural networks")
    assert len(res_ml) > 0
    assert res_ml[0][0]["chunk_id"] == "c2"

    # Test save/load
    index.save(temp_index_dir)
    
    new_index = BM25Index()
    assert new_index.load(temp_index_dir) is True
    assert len(new_index.chunks) == 3
    
    res_load = new_index.search("programming language")
    assert res_load[0][0]["chunk_id"] == "c1"
