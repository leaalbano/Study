from ArrayStack import ArrayStack
import unittest

class TestArrayStack(unittest.TestCase):
    
    def setUp(self):
        self.array_stack = ArrayStack()
    
    def test_set_up(self):
        self.assertEqual(self.array_stack.peek(), None)
        self.assertEqual(self.array_stack.size, 0)
        self.expected_array_stack = [None] * 9
        self.assertEqual(self.array_stack.backing_array, self.expected_array_stack)

    def test_push(self):
        self.array_stack.push(10)
        self.assertEqual(self.array_stack.peek(), 10)
        self.array_stack.push(20)
        self.assertEqual(self.array_stack.peek(), 20)
    
    def test_pop(self):
        self.array_stack.push(10)
        self.assertEqual(self.array_stack.pop(), 10)
        self.array_stack.push(20)
        self.array_stack.push(30)
        self.array_stack.push(40)
        self.assertEqual(self.array_stack.pop(), 40)

    def test_peek(self):
        self.array_stack.push(10)
        self.array_stack.push(20)
        self.array_stack.push(30)
        self.assertEqual(self.array_stack.pop(), 30)

    def test_size(self):
        self.array_stack.push(10)
        self.array_stack.push(20)
        self.array_stack.push(30)
        self.assertEqual(self.array_stack.size, 3)


if __name__ == '__main__':
    import sys
    sys.argv.append('-v')
    unittest.main()
