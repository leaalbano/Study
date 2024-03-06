import unittest
from book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book('Hunger Games', 'Suzanne Collins', 2008, 'Dystopian')
        self.book2 = Book('Moby Dick', 'Herman Melville', 1851, 'Adventure fiction')

    def test_classic(self):
        self.assertFalse(self.book.classic(), False)
        self.assertTrue(self.book2.classic(), True)


if __name__ == '__main__':
    unittest.main()