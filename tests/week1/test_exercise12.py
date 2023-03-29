import pytest
import app.week1.exercise12 as exercise12

def test_only_integers():
    assert exercise12.only_integers([1,"two",3.0,-2,2]) == [1,2]
