"""
Name: Martin Jiang and Terence Tong
Class: 202 - 9
"""


class Node:
    def __init__(self, data, nxt=None, prev=None):
        self.data = data
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nextStr = 'Tail' if self.next is None else self.next.data
        prevStr = 'Head' if self.prev is None else self.prev.data
        return 'Node({}, {}, {})'.format(prevStr, self.data, nextStr)


class OrderedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.num_items = 0

    '''
    Terence Tong
    adds an item to the list preserving the order of the list
    input: item
    output: None
    '''
    def add(self, item):
        newnode = Node(item)
        self.num_items += 1
        if self.head is None and self.tail is None:  # initial condition
            self.head = newnode
            self.tail = newnode
        else:
            prev = None
            curr = self.head
            while curr is not None and curr.data < newnode.data:
                prev = curr
                curr = curr.next
            if prev is None:
                self.head.prev = newnode
                newnode.next = self.head
                self.head = newnode
            elif curr is None:
                self.tail.next = newnode
                newnode.prev = self.tail
                self.tail = newnode
            else:
                prev.next = newnode
                newnode.prev = prev
                newnode.next = curr
                curr.prev = newnode

    """
    Terence Tong
    removes an item from the list
    input: item
    output: is found return index of item removed
        else return -1
    """
    def remove(self, item):
        prev = None
        curr = self.head
        index = 0
        if self.num_items == 0:
            return -1
        while curr.next is not None and curr.data != item:  # last iteration should be curr is None
            if curr.data > item:  # because it scans from left to right, the data should always be less than the item
                return -1
            prev = curr
            curr = curr.next
            index += 1
        if curr.data == item:
            self.num_items -= 1
            if prev is None and curr.next is None: # only item in list
                self.head = None
                self.tail = None
                return index
            elif prev is None: # first item in list
                self.head = self.head.next
                self.head.prev = None
                return index  # should be 0
            elif curr.next is None:  # last item in list
                self.tail = prev
                self.tail.next = None
                return index  # should be num_items - 1
            else:  # anything else
                prev.next = curr.next
                curr.next.prev = prev
                return index
        return -1


    '''
    Martin Jiang
    searches for item from head to tail
    input: item
    output: boolean
    '''
    def search_forward(self, item):
        cur = self.head  # cur is a node, allows us to loop through the linked list
        found = False  # found is a Boolean, is true when cur.data == item
        stop = False  # stop is a Boolean, is true when cur.data > item
        while cur is not None and not found and not stop:
            if cur.data == item:
                found = True
            elif cur.data > item:
                stop = True
            else:
                cur = cur.next
        return found

    '''
    Terence Tong
    searches for item from tail to head
    input: item
    output: boolean
    '''
    def search_backwards(self, item):
        if self.is_empty():
            return False
        curr = self.tail
        while curr.prev is not None and curr.data != item:
            if curr.data < item:
                return False
            curr = curr.prev
        if curr.data == item:
            return True
        return False

    '''
    Martin Jiang
    checks if list is empty
    input: None
    output: boolean
    '''
    def is_empty(self):
        return self.head is None

    '''
    Terence Tong
    returns numbers in list
    input: None
    output: integer
    '''
    def size(self):
        return self.num_items

    '''
    Martin Jiang
    find an item in the list
    input: item
    output: integer index
    '''
    def index(self, item):
        count = 0  # count is an int, holds the index number
        cur = self.head  # cur is a Node, allows us to loop through the list
        found = False  # found is a Boolean, is true when cur.data == item, if true return count
        stop = False  # stop is a Boolean, is true when cur.data is < item
        while cur is not None and not found and not stop:
            if cur.data == item:
                found = True
                return count
            elif cur.data > item:
                stop = True
            else:
                cur = cur.next
                count += 1
        return -1

    '''
    Martin Jiang
    removes and returns the item at pos
    removes and returns the item at the end
    input: None or int pos
    output: item at pos or -1
    '''
    def pop(self, pos=None):
        if self.size() == 0:
            raise IndexError
        elif pos is None or pos == self.size() - 1:
            if self.size() == 1:
                temp = self.head
                self.head = None
                self.tail = None
                self.num_items -= 1
                return temp.data
            else:
                temp = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                self.num_items -= 1
                return temp.data
        else:
            if pos > self.size() or pos < 0:
                return -1
            elif pos == 0:
                temp = self.head
                self.head = self.head.next
                self.head.prev = None
                self.num_items -= 1
                return temp.data
            elif pos <= self.size() / 2:
                index = 0  # index is an int, starts at 0
                cur = self.head  # cur is a Node, allows us to loop through front half of list
                prv = None  # prv is a None type, holds the node previous to cur
                while index < pos:
                    prv = cur
                    cur = cur.next
                    index += 1
                prv.next = cur.next
                cur.next.prev = prv
                self.num_items -= 1
                return cur.data
            else:  # pos > self.size()/2
                index = self.size() - 1  # index is an int, starts at size-1
                cur = self.tail  # cur is a Node, allows us to loop through back half of list
                nxt = None  # nxt is a None type, holds the node next to cur
                while index > pos:
                    nxt = cur
                    cur = cur.prev
                    index -= 1
                nxt.prev = cur.prev
                cur.prev.next = nxt
                self.num_items -= 1
                return cur.data

    def __repr__(self):
        curr = self.head
        str = 'List: '
        while curr is not None:
            str += curr.__repr__() + '   '
            curr = curr.next
        return str
        #return 'OrderedList({},{},{})'.format(self.head, self.tail, self.num_items)

