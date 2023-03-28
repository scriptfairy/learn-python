# Exercise 10: Write a Python function that accepts three parameters. The first
# parameter is an integer. The second is one of the following mathematical operators:
# +, -, /, or *. The third parameter will also be an integer.
#
# The function should perform a calculation and return the results. For example, if the 
# function is passed 6 * 4, it should return 24.

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

