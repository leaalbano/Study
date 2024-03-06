'''
str.count(sub[, start[, end]])
Return the number of non-overlapping occurrences of substring sub in the range [start, end].
Optional arguments start and end are interpreted as in slice notation.

If sub is empty, returns the number of empty strings between characters which is the length 
of the string plus one.

str.endswith(suffix[, start[, end]])
Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple of suffixes to look for. 
With optional start, test beginning at that position. 
With optional end, stop comparing at that position.

str.find(sub[, start[, end]])
Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

str.format(*args, **kwargs)
Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}. Each replacement field contains either the numeric 
index of a positional argument, or the name of a keyword argument. Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.
'''

import unittest

class TestString(unittest.TestCase):
    def setUp(self):
        self.string1 = str()
        self.string1 = 'Monty Python burger los angeles neutron lightly'

    def test_count(self):
        self.assertEqual(self.string1.count('y', 0, len(self.string1)), 3)
        self.assertEqual(self.string1.count('M', 0, len(self.string1)), 1)
        self.assertEqual(self.string1.count('o', 0, len(self.string1)), 4)
        self.assertEqual(self.string1.count(' ', 0, len(self.string1)), 6)

    def test_endswith(self):
        self.assertEqual(self.string1.endswith('at', 0, len(self.string1)), False)
        string2 = 'Scat'
        self.string1 = self.string1 + ' ' + string2
        self.assertEqual(self.string1.endswith('at', 0, len(self.string1)), True)
    
    def test_find(self):
        location = self.string1.find('los')
        self.assertEqual(location, 20)
        location2 = self.string1.find('alt')
        self.assertEqual(location2, -1)

    def test_isalnum(self):
        #c.isalpha(), c.isdecimal(), c.isdigit(), or c.isnumeric()
        c = "Light"
        b = "123"
        a = "Loop1"
        self.assertTrue(c.isalpha(), True)
        self.assertFalse(c.isdigit())
        self.assertTrue(b.isdigit(), True)
        self.assertTrue(a.isalnum(), True)


    

if __name__ == '__main__':
    unittest.main()
