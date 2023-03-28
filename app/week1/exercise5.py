import random
# from .exercise4 import random_10_numbers

def percentage_conversion(l):
    total = sum(l)
    return [round((x/total) * 100) for x in l]

# l = random_10_numbers()
# print(l,percentage_conversion(l))

# print([0, float('inf')])
