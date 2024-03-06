from ArrayQueue import ArrayQueue
import unittest

class TestArrayQueue(unittest.TestCase):
    
    def setUp(self):
        self.array_queue = ArrayQueue()

    def test_set_up(self):
        self.assertEqual(self.array_queue.front, 0)
        self.assertEqual(self.array_queue.size, 0)
        self.expected_array_queue = [None] * 9
        self.assertEqual(self.array_queue.backing_array, self.expected_array_queue)

    def test_enqueue(self):
        self.array_queue.enqueue(1)
        self.array_queue.enqueue(2)
        self.array_queue.enqueue(3)
        self.expected_array_queue = self.array_queue.backing_array
        self.assertEqual(self.expected_array_queue[0], 1)
        self.assertEqual(self.expected_array_queue[1], 2)
        self.assertEqual(self.expected_array_queue[2], 3)
        self.assertEqual(self.array_queue.size, 3)

    def test_peek(self):
        self.array_queue.enqueue(1)
        self.array_queue.enqueue(2)
        self.array_queue.enqueue(3)
        self.assertEqual(self.array_queue.size, 3)
        self.assertEqual(self.array_queue.peek(), 1)

    def test_dequeue(self):
        self.array_queue.enqueue(1)
        self.array_queue.enqueue(2)
        self.array_queue.enqueue(3)
        self.assertEqual(self.array_queue.peek(), 1)
        self.assertEqual(self.array_queue.dequeue(), 1)
        self.assertEqual(self.array_queue.size, 2)
        self.assertEqual(self.array_queue.peek(), 2)

    def test_get_backing_array(self):
        self.array_queue.enqueue(1)
        self.array_queue.enqueue(2)
        self.array_queue.enqueue(3)
        self.assertEqual(self.array_queue.backing_array, [1, 2, 3, None, None, None, None, None, None])

    def test_size(self):
        self.array_queue.enqueue(1)
        self.array_queue.enqueue(2)
        self.assertEqual(self.array_queue.size, 2)

    def test_case1(self):
        '''tests to see if it resizes correctly'''
        self.array_queue.enqueue(1)
        self.array_queue.enqueue(2)
        self.array_queue.enqueue(3)
        self.array_queue.enqueue(4)
        self.array_queue.enqueue(5)
        self.array_queue.enqueue(6)
        self.array_queue.enqueue(7)
        self.array_queue.enqueue(8)
        self.array_queue.enqueue(9)
        self.array_queue.enqueue(10)
        self.expected_array_queue = self.array_queue.backing_array
        self.assertEqual(self.expected_array_queue[0], 1)
        self.assertEqual(self.expected_array_queue[1], 2)
        self.assertEqual(self.expected_array_queue[2], 3)
        self.assertEqual(self.expected_array_queue[3], 4)
        self.assertEqual(self.expected_array_queue[4], 5)
        self.assertEqual(self.expected_array_queue[5], 6)
        self.assertEqual(self.expected_array_queue[6], 7)
        self.assertEqual(self.expected_array_queue[7], 8)
        self.assertEqual(self.expected_array_queue[8], 9)
        self.assertEqual(self.array_queue.size, 10)

    def test_case1(self):
        '''tests to see if dequeue works circularly'''
        self.array_queue.enqueue(1)
        self.array_queue.enqueue(2)
        self.array_queue.enqueue(3)
        self.array_queue.enqueue(4)
        self.assertEqual(self.array_queue.peek(), 1)
        self.assertEqual(self.array_queue.dequeue(), 1)
        self.assertEqual(self.array_queue.front, 1)
        print(self.array_queue.backing_array)
        self.assertEqual(self.array_queue.peek(), 2)
        self.array_queue.dequeue()
        



if __name__ == '__main__':
    import sys
    sys.argv.append('-v')
    unittest.main()
