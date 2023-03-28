import pytest
import app.week1.exercise4 as exercise4

def test_random_10_numbers():
    l = exercise4.random_10_numbers()
    assert exercise4.reverse_sort_list(l) == sorted(l,reverse=True) 
    
    
    