'''Create a Python class named Student with the following attributes:

name (string)
age (integer)
grades (list of integers)
Include methods in the class to:

Calculate the average grade of the student.
Determine if the student passed (average grade >= 60).'''

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        if len(self.grades) > 0:
            average = sum(self.grades)/len(self.grades)
            return average
        else:
            print("There are no grades given")
            return False
    
    def is_passing(self):
        if self.average_grade() >= 60:
            print("Course eval: passing")
            return True
        else:
            print("course eval: not passing")
            return False
    
    def print_details(self):
        print("Students name: ", self.name)
        print("Age: ", self.age)
        print("Grades: ", self.grades)
        print("Average grade: ", self.average_grade())
    
'''student1 = Student("Lea", 22, [85,90,80,70,90])
student1.average_grade()
student1.is_passing()
student1.print_details()
'''

