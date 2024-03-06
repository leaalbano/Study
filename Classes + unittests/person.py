'''Problem 1: Creating a Simple Class
Create a Python class named Person with the following attributes:

name (string)
age (integer)
gender (string)
Include a method in the class to print the person's details.

'''

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def print_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)

person1 = Person("Lea", 22, "Female")
person1.print_details()
