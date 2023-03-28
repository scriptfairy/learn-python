class Person:
    #class_variable = whatever
    # class_variable is shared between all the instances of the class
    # in our case we don't have such varialbe

    # Class constructor
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name.strip()

# Get instance of person and call it whatever your name
christine = Person("Christine", "Al-Thifairy")

print("Hello, my name is ", christine.first_name, " ", christine.last_name)