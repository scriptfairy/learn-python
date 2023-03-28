import random

def percentage_conversion(l):
    total = sum(l)
    if total == 0:
        n = len(l)
        return [0] * n
    return [round((x/total) * 100) for x in l]
