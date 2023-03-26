import pytest
import app.week0.person as person

def test_get_full_name():
    my_person = person.Person("Christine", "Al-Thifairy")
    assert my_person.get_full_name() == "Christine Al-Thifairy" 
    
def test_get_full_name_strips_spaces():
    my_person = person.Person(" ", "Al-Thifairy")
    assert my_person.get_full_name() == "Al-Thifairy" 