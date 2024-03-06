class ArrayQueue:
    INITIAL_CAPACITY = 9

    def __init__(self):
        """
        Constructs a new ArrayQueue.
        """
        self.backing_array = [None] * self.INITIAL_CAPACITY   
        self.front = 0
        self.size = 0

    def enqueue(self, data):
        """
        Adds the given data to the queue.

        If sufficient space is not available in the backing array, you should
        resize it to double the current length. If a resize is necessary,
        you should copy elements to the front of the new array and reset
        front to 0.

        This method should be implemented in amortized O(1) time.

        :param data: the data to add
        :raises ValueError: if data is None
        """
        if data is None:
            raise ValueError
        if self.size == len(self.backing_array):
            temp_backing_array = self.backing_array
            self.backing_array = [None] * (len(self.backing_array) * 2)
            for i in range(len(temp_backing_array)):
                self.backing_array[i] = temp_backing_array[i]
            self.front = 0
        self.backing_array[self.size + self.front] = data
        self.size += 1

    def dequeue(self):
        """
        Removes the data from the front of the queue.

        Do not shrink the backing array. If the queue becomes empty as a result
        of this call, you should explicitly reset front to 0.

        You should replace any spots that you dequeue from with None. Failure to
        do so can result in a loss of points.

        This method should be implemented in O(1) time.

        :return: the data from the front of the queue
        :raises IndexError: if the queue is empty
        """
        if self.size == 0:
            raise IndexError
        else:
            removed_value = self.peek()
            self.backing_array[self.front] = None
            self.front = self.front + 1
            self.size -= 1
            if self.size == 0:
                self.front = 0
        return removed_value
        

    def peek(self):
        """
        Retrieves the next data to be dequeued without removing it.

        This method should be implemented in O(1) time.

        :return: the next data or None if the queue is empty
        """
        if self.size == 0:
            return None
        else:
            return self.backing_array[self.front]

    def size(self):
        """
        Returns the size of the queue.

        :return: number of items in the queue
        """
        return self.size

    def get_backing_array(self):
        """
        Returns the backing array of the queue.

        :return: the backing array
        """
        return self.backing_array
