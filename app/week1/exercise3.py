# Create a list of 10 random numbers
import random
import pytest
def exercise3():
    mylist = []
    for i in range(10):
        mylist.append(random.random())
    return mylist

l = exercise3()
print(l)


