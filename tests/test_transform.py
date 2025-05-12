import pytest
from code.transform import analyze_sentiment

def test_analyze_sentiment():
    assert analyze_sentiment("I love this movie") == "positive"
    assert analyze_sentiment("I hate this movie") == "negative"
    assert analyze_sentiment("This movie is okay") == "neutral"
    assert analyze_sentiment(None) == "neutral"
