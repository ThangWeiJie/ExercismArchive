class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = -1
        self.tail = -1

    def read(self):
        if self.buffer[self.head] == None or self.head == -1:
            raise BufferEmptyException("Circular buffer is empty")

        item_to_return = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        return item_to_return

    def write(self, data):
        if self.head == -1:
            self.head += 1
            self.buffer[self.head] = data
            self.tail += 1
        else:
            self.tail = (self.tail + 1) % self.capacity
            if self.tail == self.head and self.buffer[self.tail] != None:
                raise BufferFullException("Circular buffer is full")
            
            self.buffer[self.tail] = data


    def overwrite(self, data):
        if self.tail + 1 == self.capacity or self.buffer[self.tail + 1] != None:
            self.head = (self.head + 1) % self.capacity
        self.tail = (self.tail + 1) % self.capacity
        self.buffer[self.tail] = data

    def clear(self):
        self.buffer = [None] * self.capacity
        self.head = self.tail = -1
