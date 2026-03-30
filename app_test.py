import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "app"))

from spam import check_spam

def test_spam_detected():
    result, hit = check_spam("free money win now")
    assert result == "spam"

def test_ham_detected():
    result, hit = check_spam("hello how are you")
    assert result == "ham"

def test_empty_string():
    result, hit = check_spam("")
    assert result == "ham"
    assert hit == 0

def test_single_keyword():
    result, hit = check_spam("free stuff here")
    assert result == "ham"
    assert hit == 1
