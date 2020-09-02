class Queue:

    def __init__(self, max_size):
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.list = list(range(self.max_size))
        
    def enqueue(self, value):
        self.list[self.tail] = value
        if self.tail == self.max_size - 1:
            self.tail = 0
        else:
            self.tail += 1
       
    def dequeue(self):
        x = self.list[self.head]
        if self.head == self.max_size - 1:
            self.head = 0
        else:
            self.head += 1
        return x
