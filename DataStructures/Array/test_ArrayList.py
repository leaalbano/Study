import unittest
from ArrayList import arrayList

class TestArrayList(unittest.TestCase):

        def setUp(self):
            #Create empty array of size 9
            self.array1 = arrayList(None, 9)
            
        def test_setUp(self):
             #tests setUp method
             expected_array = [None] * 9
             self.assertEqual(self.array1.backing_array, expected_array)
        
        def test_addToIndex(self):
            with self.assertRaises(ValueError, msg="Value Error"):
                #checks if valid data input
                self.array1.addToIndex(0, None)
                self.array1.addToIndex(0,"")

            with self.assertRaises(IndexError, msg="Index Error"):
                #checks if index within range of array size
                self.array1.addToIndex(-1, 0)
                self.array1.addToIndex(10, 0)
            
            self.array1.addToIndex(0,1)
            #checks if data is added at index
            self.assertEqual(self.array1.backing_array[0], 1)
        
        def test_removeAtIndex(self):
             self.array1.addToIndex(0,1)
             with self.assertRaises(IndexError, msg="Index Error"):
                self.assertEqual(self.array1.removeAtIndex(-1), msg="Index Error")
             self.assertEqual(self.array1.removeAtIndex(0), 1)

if __name__ == '__main__':
    # Add the -v option to the argument list
    import sys
    sys.argv.append('-v')
    
    # Run the unittest
    unittest.main()