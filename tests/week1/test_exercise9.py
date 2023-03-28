import pytest
import app.week1.exercise9 as exercise9

def test_replace_with_asterisk_empty_string():
    s = ""
    assert exercise9.replace_with_asterisk(s) == ""

def test_replace_with_asterisk_short_string():
    s = "123"
    assert exercise9.replace_with_asterisk(s) == "123"

def test_replace_with_asterisk_end_of_line():
    s = "12345678\n"
    assert exercise9.replace_with_asterisk(s) == "****5678\n"

def test_replace_with_asterisk():
    s = "1234-5678-9012-3456"
    assert exercise9.replace_with_asterisk(s) == "***************3456"