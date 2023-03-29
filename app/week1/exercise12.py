# ## Exercise 12:  Write a function in Python that accepts a list of any length 
# that contains a mix of non-negative integers and strings. 
# The function should return a list with only the integers in the 
# original list in the same order.

def only_integers(l):
    result = [x for x in l if isinstance(x, int) and x > 0]
    return result

my_list = [1, "two", 3.0, "four", 5, -6]
print(only_integers(my_list))