class QueueArray:
    def __init__(self, capacity):
        # the maximum number of items that can be stored in queue
        self.capacity = capacity
        self.num_items = int(0)
        self.front = 0  # index
        self.rear = 0  # index
        self.items = [None] * capacity

    # -> boolean
    def is_empty(self):
        return self.num_items == 0

    # -> boolean
    def is_full(self):
        return self.num_items == self.capacity

    # item ->
    def enqueue(self, item):
        if self.is_full():
            raise IndexError
        self.num_items += 1
        self.items[self.rear] = item
        self.rear += 1
        if self.rear == self.capacity:
            self.rear = 0

    # -> return self.queue[front]
    def dequeue(self):
        if self.is_empty():
            raise IndexError
        self.num_items -= 1
        temp = self.items[self.front]
        self.items[self.front] = None
        self.front += 1
        if self.front == self.capacity:
            self.front = 0
        return temp

    # returns the number of items in the queue
    def num_in_queue(self):
        return self.num_items

    def __repr__(self):
        return self.items

    def __eq__(self, other):
        return self.items == other.items


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def setData(self, data):
        self.data = data

    def __repr__(self):
        return self.getData()

    def __eq__(self, other):
        return self.data == other.data


class QueueLinked:
    def __init__(self, capacity):
        # the maximum number of items that can be stored in queue
        self.capacity = capacity
        self.num_items = 0
        self.front = None
        self.rear = None
    # -> boolean
    def is_empty(self):
        return self.num_items == 0

    # -> boolean
    def is_full(self):
        return self.num_items == self.capacity

    # item ->
    def enqueue(self, item):
        if self.is_full():
            raise IndexError
        node = Node(item)
        self.num_items += 1
        if self.front is None:
            self.rear, self.front = node, node
        else:
            self.rear.setNext(node)
            self.rear = node

    # -> return self.queue[front]
    def dequeue(self):
        if self.is_empty():
            raise IndexError
        self.num_items -= 1
        temp = self.front
        self.front = self.front.getNext()
        return temp.getData()

    # returns the number of items in the queue
    def num_in_queue(self):
        return self.num_items

    def __repr__(self):
        curr = self.items
        s = ''
        while curr is not None:
            s += '{}, '.format(curr.getData())
            curr = curr.getNext()
        return s

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()