import unittest
from CircularLinkedList import CircularLinkedList  

class TestCircularLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = CircularLinkedList()

    def test_set_up(self):
        self.assertIsNone(self.linked_list.head)
        self.assertEqual(self.linked_list.size, 0)

    def test_add_at_index(self):
        # Test invalid data
        with self.assertRaises(ValueError, msg="Value Error"):
            self.linked_list.add_at_index(0, None)

        # Test index out of range
        with self.assertRaises(IndexError, msg="Index Error"):
            self.linked_list.add_at_index(-1, 0)
            self.linked_list.add_at_index(10, 0)
        
        self.linked_list.add_at_index(0, 'A')
        self.linked_list.add_at_index(1, 'B')
        self.linked_list.add_at_index(2, 'C')
        self.linked_list.add_at_index(3, 'D')
        self.linked_list.add_at_index(4, 'E')
        self.assertEqual(self.linked_list.size, 5)

        current = self.linked_list.head
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), 'A')

        current = current.get_next()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), 'B')

        current = current.get_next()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), 'C')

        current = current.get_next()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), 'D')

        current = current.get_next()
        self.assertIsNotNone(current)
        self.assertEqual(current.get_data(), 'E')

        #Makes sure last node points to head
        current = current.get_next()
        self.assertIsNotNone(current)
        self.assertIs(self.linked_list.get_head(), current)

    def test_remove_at_index(self):
        # Test index out of range
        with self.assertRaises(IndexError, msg="Index Error"):
            self.linked_list.remove_at_index(-1)
            self.linked_list.remove_at_index(10)
        
        self.linked_list.add_to_front('A')
        self.linked_list.add_at_index(1, 'B')
        self.linked_list.add_at_index(2, 'C')
        self.linked_list.add_to_back('D')
        self.linked_list.print_list() #A -> B -> C -> D ->  (Head)

        self.assertEqual(self.linked_list.size, 4)

        self.assertEqual('A', self.linked_list.remove_at_index(0)) #B -> C -> D ->  (Head)
        self.linked_list.print_list()
        self.assertEqual('C', self.linked_list.remove_at_index(1)) #B -> D ->  (Head)
        self.assertEqual('D', self.linked_list.remove_at_index(self.linked_list.size)) #B ->  (Head)
        self.linked_list.print_list()
    
    def test_remove_from_front(self):
        self.linked_list.add_to_front('A')
        self.linked_list.add_at_index(1, 'B')
        self.linked_list.add_at_index(2, 'C')
        self.linked_list.add_to_back('D')
        self.linked_list.print_list() #A -> B -> C -> D ->  (Head)

        self.assertEqual(self.linked_list.remove_from_front(), "A")
        self.linked_list.print_list()
        self.assertEqual(self.linked_list.size, 3)
        self.assertEqual(self.linked_list.remove_from_front(), "B")
        self.linked_list.print_list()
        self.assertEqual(self.linked_list.size, 2)

    def test_remove_from_back(self):
        self.linked_list.add_to_front('A')
        self.linked_list.add_at_index(1, 'B')
        self.linked_list.add_at_index(2, 'C')
        self.linked_list.add_to_back('D')
        self.linked_list.print_list() #A -> B -> C -> D ->  (Head)

        self.assertEqual(self.linked_list.remove_from_back(), "D")
        self.linked_list.print_list()
        self.assertEqual(self.linked_list.size, 3)
        self.assertEqual(self.linked_list.remove_from_back(), "C")
        self.linked_list.print_list()
        self.assertEqual(self.linked_list.size, 2)

    def test_remove_last_occurance(self):
        self.linked_list.add_to_front('A')
        self.linked_list.add_at_index(1, 'B')
        self.linked_list.add_at_index(2, 'C')
        self.linked_list.add_to_back('D')
        self.linked_list.print_list() #A -> B -> C -> D ->  (Head)

        self.assertEqual(self.linked_list.size, 4)
        self.assertEqual(self.linked_list.remove_last_occurrence('A'), 'A')
        self.assertEqual(self.linked_list.size, 3)
        self.assertEqual(self.linked_list.remove_last_occurrence('C'), 'C')
        self.assertEqual(self.linked_list.size, 2)
        self.linked_list.print_list()

    def test_size(self):
        self.linked_list.add_to_front('A')
        self.assertEqual(self.linked_list.size, 1)

    def test_size2(self):
        self.linked_list.add_to_front('A')
        self.linked_list.add_to_front('B')
        self.assertEqual(self.linked_list.size, 2)
    
    def test_size3(self):
        self.linked_list.add_to_front('A')
        self.assertEqual(self.linked_list.size, 1)
        self.linked_list.remove_from_back()
        self.assertEqual(self.linked_list.size, 0)

    def test_size4(self):
        self.linked_list.add_to_front('A')
        self.assertEqual(self.linked_list.size, 1)
        self.linked_list.add_at_index(1, 'B')
        self.assertEqual(self.linked_list.size, 2)
        self.linked_list.add_to_back('C')
        self.assertEqual(self.linked_list.size, 3)

    def test_size5(self):
        self.linked_list.add_to_front('A')
        self.assertEqual(self.linked_list.size, 1)
        self.linked_list.remove_from_front()
        self.assertEqual(self.linked_list.size, 0)
        self.linked_list.remove_from_front()
        self.assertRaises(IndexError)

    def test_size6(self):
        self.linked_list.add_to_back('A')
        self.assertEqual(self.linked_list.size, 1)
        self.linked_list.add_to_back('B')
        self.assertEqual(self.linked_list.size, 2)
        self.linked_list.add_to_back('C')
        self.assertEqual(self.linked_list.size, 3)     

    
    def test_size7(self):
        self.linked_list.add_to_back('A')
        self.assertEqual(self.linked_list.size, 1)
        self.linked_list.add_to_back('B')
        self.assertEqual(self.linked_list.size, 2)
        self.linked_list.add_to_back('C')
        self.assertEqual(self.linked_list.size, 3)     
        self.linked_list.remove_at_index(2)    
        self.assertEqual(self.linked_list.size, 2)     

    def test_size8(self):
        self.linked_list.add_to_front('B')
        self.assertEqual(self.linked_list.size, 1)
        self.linked_list.add_to_front('A')
        self.assertEqual(self.linked_list.size, 2)
        self.assertEqual(self.linked_list.head.data, 'A')

    def test_size9(self):
        self.linked_list.add_to_front('B')
        self.assertEqual(self.linked_list.size, 1)
        self.linked_list.add_to_front('A')
        self.assertEqual(self.linked_list.size, 2)
        self.assertEqual(self.linked_list.head.data, 'A')
        self.assertEqual(self.linked_list.head.get_next().get_data(), 'B')

    def test_size10(self):
        self.linked_list.add_to_front('A')
        self.assertEqual(self.linked_list.size, 1)
        self.assertEqual(self.linked_list.head.data, 'A')
        # print("value" + self.linked_list.head.next.data)
        # self.assertEqual(self.linked_list.head.next, None)

    def test_size11(self):
        self.linked_list.add_to_front('A')
        self.assertEqual(self.linked_list.size, 1)
        self.assertEqual(self.linked_list.head.data, 'A')
        self.linked_list.add_to_back('B')
        self.assertEqual(self.linked_list.size, 2)
        self.assertEqual(self.linked_list.head.get_next().get_data(), 'B')

    def test_size12(self):
        self.linked_list.add_to_front('A')
        self.assertEqual(self.linked_list.size, 1)
        self.assertEqual(self.linked_list.head.data, 'A')
        self.linked_list.add_to_back('B')
        self.assertEqual(self.linked_list.size, 2)
        self.assertEqual(self.linked_list.head.get_next().get_data(), 'B')
        self.linked_list.add_to_back('C')
        self.assertEqual(self.linked_list.size, 3)
        self.assertEqual(self.linked_list.head.get_next().get_next().get_data(), 'C')

    def test_size13(self):
        self.linked_list.add_to_front('A')
        self.assertEqual(self.linked_list.size, 1)
        self.assertEqual(self.linked_list.head.data, 'A')
        self.linked_list.add_to_back('B')
        self.assertEqual(self.linked_list.size, 2)
        self.assertEqual(self.linked_list.head.get_next().get_data(), 'B')
        self.linked_list.add_to_back('C')
        self.assertEqual(self.linked_list.size, 3)
        self.assertEqual(self.linked_list.head.get_next().get_next().get_data(), 'C')
        self.linked_list.add_to_front('D')
        self.assertEqual(self.linked_list.size, 4)
        self.assertEqual(self.linked_list.head.get_data(), 'D')

    def test_size14(self):
        self.linked_list.add_to_front('A')
        self.assertEqual(self.linked_list.size, 1)
        self.assertEqual(self.linked_list.head.data, 'A')
        self.linked_list.add_to_back('B')
        self.assertEqual(self.linked_list.size, 2)
        self.assertEqual(self.linked_list.head.get_next().get_data(), 'B')
        self.linked_list.add_to_back('C')
        self.assertEqual(self.linked_list.size, 3)
        self.assertEqual(self.linked_list.head.get_next().get_next().get_data(), 'C')
        self.linked_list.add_to_front('D')
        self.linked_list.print_list()
        self.assertEqual(self.linked_list.size, 4)
        self.assertEqual(self.linked_list.head.get_data(), 'D')
        # self.assertEqual(self.linked_list.head.get_next().get_data(), 'A')
        self.linked_list.print_list()

    # not working, similar scenario as above
    def test_size16(self):
        self.linked_list.add_to_back('B')
        self.assertEqual(self.linked_list.size, 1)
        self.assertEqual(self.linked_list.head.data, 'B')
        self.linked_list.add_to_back('C')
        self.assertEqual(self.linked_list.size, 2)
        self.assertEqual(self.linked_list.head.get_next().get_data(), 'C')
        self.linked_list.add_to_back('D')
        self.assertEqual(self.linked_list.size, 3)
        self.assertEqual(self.linked_list.head.get_next().get_next().get_data(), 'D')
        self.linked_list.add_to_front('A')
        self.linked_list.print_list()
        self.assertEqual(self.linked_list.size, 4)
        self.assertEqual(self.linked_list.head.get_data(), 'A')
        # self.assertEqual(self.linked_list.head.get_next().get_data(), 'B')
        self.linked_list.print_list()

    def test_size17(self):
        self.linked_list.add_to_back('B')
        self.assertEqual(self.linked_list.size, 1)
        self.assertEqual(self.linked_list.head.data, 'B')
        self.linked_list.add_to_back('C')
        self.assertEqual(self.linked_list.size, 2)
        self.assertEqual(self.linked_list.head.get_next().get_data(), 'C')
        self.linked_list.add_to_back('D')
        self.assertEqual(self.linked_list.size, 3)
        self.assertEqual(self.linked_list.head.get_next().get_next().get_data(), 'D')
        self.linked_list.remove_from_back()
        self.linked_list.print_list()
        self.assertEqual(self.linked_list.size, 2)
        self.assertEqual(self.linked_list.head.get_data(), 'B')
        self.assertEqual(self.linked_list.head.get_next().get_data(), 'C')


    def test_size18(self):
        self.linked_list.add_to_back('B')
        self.assertEqual(self.linked_list.size, 1)
        self.assertEqual(self.linked_list.head.data, 'B')
        self.linked_list.add_to_back('C')
        self.assertEqual(self.linked_list.size, 2)
        self.assertEqual(self.linked_list.head.get_next().get_data(), 'C')
        self.linked_list.add_to_back('D')
        self.assertEqual(self.linked_list.size, 3)
        self.assertEqual(self.linked_list.head.get_next().get_next().get_data(), 'D')
        self.linked_list.remove_from_back()
        self.linked_list.print_list()
        self.assertEqual(self.linked_list.size, 2)
        self.assertEqual(self.linked_list.head.get_data(), 'B')
        self.assertEqual(self.linked_list.head.get_next().get_data(), 'C')
        self.linked_list.remove_from_back()
        self.linked_list.print_list()
        self.assertEqual(self.linked_list.size, 1)
        self.assertEqual(self.linked_list.head.get_data(), 'B')
        self.assertEqual(self.linked_list.head.get_next().get_data(), 'B')

    # when you remove two in a row, there is an infinite loop
    def test_size(self): 
        self.linked_list.add_to_front('A')
        self.linked_list.add_to_front('B')
        self.linked_list.add_to_front('C')
        self.linked_list.add_to_front('D')
        self.linked_list.add_to_front('E')
        self.linked_list.remove_from_back()
        self.linked_list.remove_from_back()
        self.assertEqual(self.linked_list.size, 3)

        


if __name__ == '__main__':
    import sys
    sys.argv.append('-v')
    unittest.main()
