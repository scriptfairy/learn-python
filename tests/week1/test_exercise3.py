import pytest
import app.week1.exercise3 as exercise3

def test_exercise3():
    result = exercise3.exercise3()
    assert len(result) == 10 
    
    