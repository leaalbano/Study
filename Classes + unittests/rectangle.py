'''Create a Python class named Rectangle with the following attributes:

length (float)
width (float)

Include methods in the class to:
Calculate the area of the rectangle.
Calculate the perimeter of the rectangle.
Determine if the rectangle is a square.'''

class Rectangle:
    def __init__(self, length = 0.0, width = 0.0):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        if area < 0:
            return ValueError
        else:
            print("The area is: ", area)
            return area
    
    def perimeter(self):
        perimeter = 2*(self.width) + 2*(self.length)
        print("The perimeter is: ", perimeter)
        return perimeter
    
    def is_square(self):
        if self.length == self.width:
            print("Is a square")
            return True
        else:
            print("Not a square")
            return False

'''rectangle1 = Rectangle(5.0, 6.0)
rectangle1.area()
rectangle1.perimeter()
rectangle1.is_square()
'''