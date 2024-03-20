class ArrayStack:
    '''LIFO'''
    INITIAL_CAPACITY = 9

    def __init__(self):
        self.backing_array = [None] * self.INITIAL_CAPACITY
        self.size = 0

    def push(self, data):
        '''Adds the given data onto the stack. The given element becomes the
     * top-most element of the stack.
     *
     * If sufficient space is not available in the backing array, you should
     * resize it to double the current length.
     *
     * This method should be implemented in amortized O(1) time.
     *
     * @param data the data to add
     * @throws IllegalArgumentException if data is null
     */'''
        if data == None:
            return ValueError
        if self.size == len(self.backing_array):
            temp_array = self.backing_array #old array contents
            self.backing_array = [None]*(len(self.backing_array)*2) #empty resized array
            for i in range(len(temp_array)):
                self.backing_array[i] = temp_array[i]
            
        self.backing_array[self.size] = data
        self.size += 1
       

    def pop(self):
        '''Removes and returns the top-most element on the stack.
     *
     * Do not shrink the backing array.
     *
     * You should replace any spots that you pop from with null. Failure to do
     * so can result in a loss of points.
     *
     * This method should be implemented in O(1) time.
     *
     * @return the data from the top of the stack
     * @throws java.util.NoSuchElementException if the stack is empty'''
        if self.size == 0:
            raise IndexError("Stack is empty")
        temp = self.peek()
        self.backing_array[self.size-1] = None
        return temp


    def peek(self):
        '''Retrieves the next element to be popped without removing it.
     *
     * This method should be implemented in O(1) time.
     *
     * @return the next data or null if the stack is empty'''
        if self.size == 0:
            return None
        else:
            return self.backing_array[self.size-1]
        
    def size(self):
        return self.size

    def getBackingArray(self):
        return self.backing_array


