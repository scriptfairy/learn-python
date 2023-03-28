import pytest
import app.week1.exercise10 as exercise10

def test_calculate_with_invalid_operator():
    operator = "?"
    assert exercise10.calculate(1,2,operator) == "Invalid operator"

def test_calculate():
    operator = "+"
    assert exercise10.calculate(1,2,operator) == 3
