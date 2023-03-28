import re

## Exercise 9: Write a function in Python that accepts a credit card number. It should return a string where all the characters are 
#  hidden with an asterisk except the last four.
def replace_with_asterisk(string):
    # define the pattern
    pattern = r'.(?=.{4})'

    # define the replacement
    replacement = '*'

    return re.sub(pattern,replacement,string)

# s = "123456_**78-!!!!__90988"
# print(replace_with_asterisk(s))
