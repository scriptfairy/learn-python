# Create a list of 10 random numbers
import random

def random_10_numbers():
    mylist = []
    for i in range(10):
        mylist.append(random.randint(1,100))
    return mylist

def reverse_sort_list(l):
    return sorted(l,reverse=True)

# l = random_10_numbers()
# print(l, reverse_sort_list(l))
