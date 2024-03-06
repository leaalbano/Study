import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle1 = Rectangle(5.0, 6.0)
        self.rectangle2 = Rectangle(0, 2.0)
        self.rectangle3 = Rectangle(-3.0, 9.0)
    
    def test_area(self):
        self.assertEqual(self.rectangle1.area(), 30.0)
        self.assertEqual(self.rectangle2.area(), 0)
        self.assertEqual(self.rectangle3.area(), ValueError)

if __name__ =='__main__':
    unittest.main()