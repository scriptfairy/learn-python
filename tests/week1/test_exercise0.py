import pytest
import app.week1.exercise0 as exercise0

def test_print_hello_world(capfd):
    exercise0.print_hello_world()
    #  output is captured using the capfd.readouterr() method
    captured = capfd.readouterr()
    # by default the print() function in Python adds a new line 
    # character \n at the end of the output that it prints.
    assert captured.out == "Hello, world!\n"