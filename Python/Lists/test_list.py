'''
list.append(x) -
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable) -
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x) - 
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) 
inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x) - 
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
starts at 0 

list.pop([i]) - 
Remove the item at the given position in the list, and return it. If no index is specified,
a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

list.clear() - 
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]]) - 
Return zero-based index in the list of the first item whose value is equal to x. 
Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation 
and are used to limit the search to a particular subsequence of the list. 
The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x) - 
Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False) - 
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse() - 
Reverse the elements of the list in place.

list.copy() - 
Return a shallow copy of the list. Equivalent to a[:].
ex: STOCK | PRICE | BUY/SELL
'''

import unittest
class TestListMethods(unittest.TestCase):

    def setUp(self):
        self.list1 = list()
        self.list1.append('Apple')
        self.list1.append('Orange')
        self.list1.append('Lemon')

    def test_append(self):
        self.list1.append('One')
        self.assertEqual(self.list1[3], 'One')
        self.list1.append('Two')
        self.list1.append('Three')
        self.assertEqual(self.list1[0], 'Apple')

    def test_extend(self):
        list2 = list()
        list2.append(1)
        list2.append(2)
        list2.append(3)
        self.list1.extend(list2)
        self.assertEqual(self.list1[3], 1)
        self.assertEqual(self.list1[3:], list2)
    
    def test_insert(self):
        self.list1.insert(1, 'Red')
        self.assertEqual(self.list1[1], 'Red')
        self.list1.insert(2, 'Hi')
        self.assertEqual(self.list1[2], 'Hi')

    def test_remove(self):
        self.list1.append('Apple')
        self.assertEqual(len(self.list1), 4)
        self.assertEqual(self.list1[0], 'Apple')
        self.list1.remove('Apple')
        self.assertEqual(len(self.list1), 3)
        self.assertEqual(self.list1[0], 'Orange')
        self.list1.remove('Apple')
        self.assertEqual(len(self.list1), 2)
        self.assertEqual(self.list1[3:], [])
        with self.assertRaises(ValueError):
            self.list1.remove('Apple')
        
    def test_pop(self):
        with self.assertRaises(IndexError):
            self.list1.pop(3)
        self.assertEqual(self.list1[-1], 'Lemon')
        self.list1.pop()
        self.assertEqual(self.list1[-1], 'Orange' )
        self.list1.pop(0)
        self.assertEqual(self.list1[0], 'Orange')

    def test_clear(self):
        self.assertEqual(self.list1, ['Apple', 'Orange', 'Lemon'])
        self.list1.clear()
        self.assertEqual(self.list1, [])
        self.list1.append('test')
        self.assertEqual(self.list1.clear(), None)

    def test_index(self):
        with self.assertRaises(ValueError):
            self.list1.remove('Apple')
            self.assertEqual(self.list1.index('Apple', 0, len(self.list1)), 0)
        self.list1.append('Apple')
        self.assertEqual(self.list1.index('Apple'), 2)

    def test_count(self):
        self.list1.append('Lemon')
        self.list1.append('Lemon')
        self.list1.append('Lemon')
        self.assertEqual(self.list1.count('Lemon'), 4)
        self.list1.remove('Lemon')
        self.assertEqual(self.list1.count('Lemon'), 3)
        
    def test_sort(self):
        self.list1.append('banana')
        self.list1.append('cherry')
        self.list1.append('pear')
        self.list1.sort(key = len, reverse=True)
        self.assertEqual(self.list1, ['Orange', 'banana', 'cherry', 'Apple', 'Lemon', 'pear'])

    def test_reverse(self):
        #['Apple', 'Orange', 'Lemon']
        self.list1.reverse()
        self.assertEqual(self.list1[0], 'Lemon')
        self.list1.append('Pear')
        self.list1.reverse()
        self.assertEqual(self.list1[0], 'Pear')

    def test_copy(self):
        self.list1.copy()
        print(self.list1)

    def test_slice(self):
        list2 = list()
        list2.append('A')
        list2.append('B')
        list2.append('C')
        list2.append('D')
        list2.append('E')
        list2.append('A')
        list2.append('B')
        list2.append('C')
        list2.append('D')
        list2.append('E')
        #Replace every other letter with a lowercase version of it
        for i in (range(1, len(list2), 2)):
            list2[i] = str.lower(list2[i])
        print(list2)

if __name__ == '__main__':
    unittest.main()