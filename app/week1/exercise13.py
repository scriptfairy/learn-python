# ## Exercise 13: Create a Python function that accepts a string. 
# The function should return a string, with each character in the original 
# string doubled. If you send the function “now” as a parameter, 
#it should return “nnooww,” and if you send “123a!”, it should return “112233aa!!”.

def double_string(string):
    result = ""
    # In python when loop through string, each ch is also a string of just one char
    # In python when multipy a string by an integer, the result is a new string consist
    # of the original string repeated specific number of times. 
    for ch in string:
        #print(type(ch))
        result += ch * 2
    return result

string = "zazu"
print(double_string(string))
