import pytest
import app.week0.hello as hello

def test_add_numbers():
    assert hello.add_numbers(2, 3) == 5, "result must equal 5"
    assert hello.add_numbers(0, 0) == 0
    assert hello.add_numbers(-2, 2) == 0

def test_multiply_numbers():
    assert hello.multiply_numbers(2, 3) == 6
    assert hello.multiply_numbers(0, 0) == 0
    assert hello.multiply_numbers(-2, 2) == -4