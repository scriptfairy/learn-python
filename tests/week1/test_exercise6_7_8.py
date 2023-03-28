import pytest
import app.week1.exercise6_7_8 as exercise6_7_8


def test_quicksort_empty_list():
    l = []
    assert exercise6_7_8.quicksort(l) == []

def test_quicksort():
    l = ["Sir Pounce-a-Lot", "Captain Fluffernutter", "Meowly Cyrus"]
    assert exercise6_7_8.quicksort(l) == ["Captain Fluffernutter", "Meowly Cyrus", "Sir Pounce-a-Lot"]

