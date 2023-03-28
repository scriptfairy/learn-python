import random
from exercise4 import random_10_numbers

def percentage_conversion(l):
    total = sum(l)
    return [round((x/total) * 100) for x in l]

# def random_10_numbers():
#     mylist = []
#     for i in range(10):
#         mylist.append(random.randint(1,100))
#     return mylist

l = random_10_numbers()
print(l,percentage_conversion(l))


    