import pytest
import app.week1.exercise13 as exercise13

def test_double_string():
    assert exercise13.double_string("zazu") == "zzaazzuu"

def test_double_string_empty():
    assert exercise13.double_string("") == ""
