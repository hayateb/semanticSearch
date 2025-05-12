from semanticSearch.cleaning.preprocesser import preprocess_text
def test_preprocess_text():
    test_text = "This is a sample text with punctuation! And some stopwords."
    result = preprocess_text(test_text)
    re = "sample text punctuation stopwords"
    assert result == re