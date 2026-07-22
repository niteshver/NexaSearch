from src.quality.quality_filter import QualityFilter

def test_quality_filter_length():
    q_filter = QualityFilter(min_words=10, max_words=50)
    
    # Too short
    short_text = "Hello world."
    assert q_filter.evaluate_quality(short_text) == 0.0
    
    # Good length
    good_text = "This is a sentence. This is another sentence. We have more than ten words now in our content."
    assert q_filter.evaluate_quality(good_text) > 0.0

def test_quality_filter_spam():
    q_filter = QualityFilter(min_words=5, max_words=100)
    
    clean_text = "This is a normal academic research paper discussing deep learning neural networks."
    spam_text = "Click here to buy now cheap pharmacy viagra or make money online casino."
    
    clean_score = q_filter.evaluate_quality(clean_text)
    spam_score = q_filter.evaluate_quality(spam_text)
    
    assert clean_score > spam_score
