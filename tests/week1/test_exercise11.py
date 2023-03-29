import pytest
import app.week1.exercise11 as exercise11

def test_calculate_discounted_price():
    assert exercise11.calculate_discounted_price(100,20) == 80.00
