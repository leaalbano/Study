import unittest
from student import Student

class TestStudent(unittest.TestCase):
    def testConst(self):
        student1 = Student("Lea", 22, [85,90,80,70,90])
        student2 = Student("Anon", 21, [60,40,50,75,70])
        student3 = Student("Anon", 21, [])

    def test_average_grade(self):
        self.assertEqual(self.student1.average_grade(), 83.0)
        self.assertEqual(self.student2.average_grade(), 59.0)
        self.assertEqual(self.student3.average_grade(), False)

    def test_is_passing(self):
        self.assertTrue(self.student1.is_passing(), True)
        self.assertFalse(self.student2.is_passing(), False)

if __name__ == '__main__':
    unittest.main()
    
    