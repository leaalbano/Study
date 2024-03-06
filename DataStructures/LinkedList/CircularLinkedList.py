from LinkedListNode import LinkedListNode

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    '''
     * Adds the element to the index specified.
     *
     * Adding to indices 0 and {@code size} should be O(1), all other cases are
     * O(n).
     *
     * @param index the requested index for the new element
     * @param data the data for the new element
     * @throws IndexOutOfBoundsException if index is negative or
     * index > size
     * @throws IllegalArgumentException if data is null
     '''
    def add_at_index(self, index, data): 
        #O(n)
        if data == None:
            raise ValueError
        if index < 0 or index > self.size:
            raise IndexError
        #a linked list node object
        new_node = LinkedListNode(data)
        #variable to traverse the linked list
        current = self.head
        if self.size == 0:
            #O(1)
            '''If LList is empty, we set the head to new_node and
            set_next to itself because its a circular LList'''
            self.head = new_node
            self.head.set_next(self.head)
        elif index == 0:
            #O(1)
            '''Add to front of LList. Copy head node's data to new node, 
            then head node will point to new node after'''
            new_node.set_next(self.head.get_next())
            self.head = new_node
        elif index == self.size:
            #O(n)
            '''Add to end of LList. Need to traverse LList to find the node that points to head.
            Make temp point to new node'''
            while current.get_next() != self.head:
                current = current.get_next()
            new_node.set_next(current.get_next())
            new_node.set_data(data)
            current.set_next(new_node)
        else:
            #O(n)
            '''Adding to middle of LList. Need to traverse LList to find node that is before target index.'''
            for i in range(index - 1):
                current = current.get_next()
            new_node.set_next(current.get_next())
            current.set_next(new_node)
        self.size += 1

    def add_to_front(self, data):
        return self.add_at_index(0, data)

    def add_to_back(self, data):
        return self.add_at_index(self.size, data)

    def remove_at_index(self, index):
        if index < 0 or index > self.size:
            raise IndexError
        #stores index data
        temp = None
        #iterates through the linkedlist
        current = self.head
        if index == 0:
            temp = self.head.get_data()
            self.head.set_data(self.head.get_next().get_data())
            self.head.set_next(self.head.get_next().get_next())
        elif index == self.size:
            while current.get_next().get_next() != self.head:
                current = current.get_next()
            temp = current.get_next().get_data()
            current.set_next(current.get_next().get_next())
        else:
            for i in range(index - 1):
                current = current.get_next()
            temp = current.get_next().get_data()
            current.set_next(current.get_next().get_next())

        self.size -= 1
        return temp
    
    def remove_from_front(self):
        return self.remove_at_index(0)

    def remove_from_back(self):
        return self.remove_at_index(self.size-1)
    
    def remove_last_occurrence(self, data):
        if data is None:
            raise ValueError
        if self.size == 0:
            return None
        
        prev = None
        current = self.head
        next = current.get_next()
        
        if current.get_data() == data:
            if self.size == 1:
                # If there is only one node in the list
                self.head = None
            else:
                # If the target data is in the first node
                self.head = next
            self.size -= 1
            return data

        while next != self.head:
            prev = current
            current = next
            next = current.get_next()

            if current.get_data() == data:
                prev.set_next(next)
                self.size -= 1
                return data
        else:
            # Target data not found
            return None

                    
    def get(self, index):
        if index < 0 or index > self.size:
            raise IndexError
        elif index == 0:
            return self.head.get_data()
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.get_next()
            return temp.get_data()
        
    def get_head(self):
        return self.head
        
    def print_list(self):
            if self.size == 0:
                print("Empty Linked List")
            else:
                current = self.head
                print("Head: " + str(self.head.get_data()))
                for i in range(self.size):
                    print(current.get_data(), end=" -> ")
                    current = current.get_next()
                    if current == self.head:
                        break
                print(" (Head)")
    
    def size(self):
        return self.size
        



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''if data == None:
    raise ValueError
if index < 0 or index > self.size:
    raise IndexError

#we create the nodes using LinkedListNode class
new_node = LinkedListNode(data)
#beginning of linkedlist, can use it to iterate through linkedlist later
current = self.head

if self.size == 0:
#When list is empty, we set the new_node as head and 
#set next pointer to itself
    self.head = new_node
    self.head.set_next(self.head)
elif index == 0:
#When adding node to front of list
    #new node will copy where head is pointing
    new_node.set_next(self.head.get_next())
    #head will reference new node because it's added to the front
    self.head.set_next(new_node)
    #set new data to head
    self.head.set_data = data
elif index == self.size:
#when adding node to end of list
    #iterate the linkedlist to find the last node
    #last node is always pointing to the head
    while current.get_next() != self.head:
        current = current.get_next()
    #when you find the last node, make it point to the node we are adding
    #then make the new node point to head
    current.set_next(new_node)
    new_node.set_next(self.head)
    new_node.set_data = data
else:
#Adding node to ith index in linkedlist
    #we want to find the node that will point to newNode
    for i in range(index - 1):
        current = current.next
    new_node.set_next(current.next)
    current.next = new_node
self.size += 1

def add_to_front(self, data):
# Your implementation here
pass

def add_to_back(self, data):
# Your implementation here
pass

def remove_at_index(self, index):
# Your implementation here
pass

def remove_from_front(self):
# Your implementation here
pass

def remove_from_back(self):
# Your implementation here
pass

def remove_last_occurrence(self, data):
# Your implementation here
pass

def to_array(self):
# Your implementation here
pass

def is_empty(self):
# Your implementation here
pass

def clear(self):
# Your implementation here
pass

def size(self):
# Your implementation here
pass

def get_head(self):
# Your implementation here
pass
'''