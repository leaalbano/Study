class arrayList:
    #public var
    INITIAL_CAPACITY = 9  

    def __init__(self, backing_array, size):     
        #protected var
        self.backing_array = [None] * self.INITIAL_CAPACITY   
        self.size = 0

    #Adds the element to the specified index.

    #Remember that this add may require elements to be shifted.

    #Must be amortized O(1) for index size and O(n) for all other cases.

    #If while adding an element, the ArrayList does not have enough space, 
    #you should regrow the backing array to twice its old capacity

    #param index: The index at which to add the new element
    #param data: The element to add at the specified index
    #raises IndexError: If index is less than 0 or greater than size
    #raises ValueError: If temp is None

    #ex: addToIndex(10,1)   adds 10 to index 1 of backingArray
    def addToIndex(self, index, data):
        if data is None:
            raise ValueError("Value Error")
        elif index < 0 or index > self.size:
            raise IndexError("Index Error")
        else:
            #Check if backing_array can accept one more element
            if len(self.backing_array) < (self.size + 1):
                #hold backing_array contents in temp before resizing
                temp_array = self.backing_array
                #Created new empty backing_array twice the size of previous backing_array
                self.backing_array = [None] * (len(self.backing_array) * 2)
                #Add array contents into resized backing_array
                for i in range(len(temp_array)):
                    self.backing_array[i] = temp_array[i]
            if index == 0:
                for i in range(self.size, 0, -1):
                    self.backing_array[i] = self.backing_array[i-1]
                self.backing_array[0] = data
            elif index == self.size:
                self.backing_array[self.size] = data
            else:
                for i in range(self.size, index - 1, -1):
                    self.backing_array[i] = self.backing_array[i+1]
            #Add the element to specified index
            self.backing_array[index] = data
            self.size += 1
    
    def addToFront(self, data):
        self.addToIndex(0, data)
    
    def addToBack(self, data):
        self.addToIndex(self.size, data)
    
    # Parameters:
    # index - the index of the element to be removed
    # Returns:
    # the element that was removed from the list
    # Throws:
    # IndexOutOfBoundsException - if the index is out of range (index < 0 || index >= size())'''
    def removeAtIndex(self, index):
        if index < 0 or index > self.size - 1:
            raise IndexError("Index Error")
        else:
            #back of array
            if index == self.size-1:
                temp_array = self.backing_array[index]
                self.backing_array[index] = None
                return temp_array
            else:
                #Index value to remove
                temp_array = self.backing_array[index]
                #remove the value from array
                self.backing_array[index] = None
                #shift array contents left
                for i in range(index, self.size-1):
                    self.backing_array[i] = self.backing_array[i+1]
                    #set end of current array to None
                self.backing_array[self.size] = None
                #Reduce array size by 1
                self.size -= 1
                return temp_array
            
    # Removes and returns the first element in the list.
    # Remember that this remove may require elements to be shifted.
    # Must be O(n).
    def removeFromFront(self):
        self.removeAtIndex(0)

    # Removes and returns the last element in the list.
    # Must be O(1).
    def removeFromBack(self):
        self.removeAtIndex(self.size-1)

    # Returns the element at the given index.
    # Must be O(1).
    def get(self, index):
        if index < 0 or index > self.size-1:
            raise IndexError
        else:
            return self.backing_array(index)
        

    # Finds the index at which the given data is located in the ArrayList.
    # If there are multiple instances of the data in the ArrayList, then return
    # the index of the last instance.
    # Be sure to think carefully about whether value or reference equality
    # should be used.
    # Must be O(n), but consider which end of the ArrayList to start from.
    #@return the last index of the data or -1 if the data is not in the list
    def lastIndexOf(self, data):
        if data == None:
            raise ValueError
        else:
            #From right to left
            for i in range(self.size-1,0,-1):
                if self.backing_array[i] == data:
                    return i
            else:
                return -1

    # Returns a boolean value representing whether or not the list is empty.
    # Must be O(1).
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False


    # Clears the list. Resets the backing array to a new array of the initial
    # capacity.
    # Must be O(1).
    def clear(self):
        self.backing_array = [None] * self.INITIAL_CAPACITY
        self.size = 0   

    # Returns the size of the list as an integer.
    # For grading purposes only. You shouldn't need to use this method since
    # you have direct access to the variable.
    def size(self):
        return self.size

    # Returns the backing array for this list.
    # For grading purposes only. You shouldn't need to use this method since
    # you have direct access to the variable.
    def getBackingArray(self):
        return self.backing_array