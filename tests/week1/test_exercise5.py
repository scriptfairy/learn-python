import pytest
import app.week1.exercise5 as exercise5


def test_percentage_conversion_of_all_zero_values():
    l = [0, 0, 0]
    assert exercise5.percentage_conversion(l) == [0, 0, 0]

def test_percentage_conversion_with_negative_values_summing_to_zero():
    l = [-1, -1]
    assert exercise5.percentage_conversion(l) == [50, 50]

def test_percentage_conversion_with_a_zero_value():
    l = [1, 0, 3]
    assert exercise5.percentage_conversion(l) == [25, 0, 75]

def test_percentage_conversion():
    l = [1, 2, 3]
    assert exercise5.percentage_conversion(l) == [17, 33, 50]
