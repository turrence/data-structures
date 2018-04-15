# Name: Terence Tong
# Class: CSC 202 - 9

# key things about the MaxHeap class,
# index[0] is empty,
# index[1] is the parent node,
# index[even] are left nodes
# index[odd] are right nodes
# ask about what the heap contents is supposed to return


class MaxHeap:
    def __init__(self, capacity=50):
        self.heapList = [0]
        self.currentSize = 0
        self.capacity = capacity


    # inserts “item” into the heap, returns true if successful, false if there is no room in the heap
    # item -> boolean
    def insert(self, item):
        if self.currentSize == self.capacity:
            return False
        self.currentSize += 1
        self.heapList.append(item)
        self.perc_up(self.currentSize)
        return True

    # returns max without changing the heap and return None if not found
    # None -> item or None
    def find_max(self):
        return None if self.is_empty() else self.heapList[1]

    # returns max and removes it from the heap and restores the heap property and return None if heap is empty
    # None -> None or int
    def del_max(self):
        #print('deleting')
        if self.is_empty():
            return None
        tmp = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.perc_down(1)
        return tmp

    # returns a list of contents of the heap in the order it is stored internal to the heap.
    # (This may be useful for in testing your implementation.)
    # None ->  String
    def heap_contents(self):
        return self.heapList[1:]

    # Method buildHeap that has a single explicit argument “list of int” and builds a heap using the bottom up method
    # discussed in class. It should return True if the build was successful and False if the capacity of the MaxHeap
    # object is not large enough to hold the “array of int” argument.
    # list of int -> list of int
    def build_heap(self, alist):
        if len(alist) > self.capacity:
            return False
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1
        return True

    # returns True if the heap is empty, false otherwise
    # None -> boolean
    def is_empty(self):
        return self.currentSize == 0

    # returns True if the heap is full, false otherwise
    # None -> boolean
    def is_full(self):
        return self.currentSize == self.capacity

    # this is the maximum number of a entries the heap can hold - 1 less than the number of entries that the array
    # allocated to hold the heap can hold.
    # None -> int
    def get_heap_cap(self):
        return self.capacity

    # the actual number of elements in the heap, not the capacity
    # None -> boolean
    def get_heap_size(self):
        return self.currentSize

    # where the parameter i is an index in the heap and perc_down moves the element stored at that location to its
    # proper place in the heap rearranging elements as it goes. Since this is an internal method we will assume that
    # the element is either in the correct position or the correct position is below the current position.
    # index -> None
    def perc_down(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    # helper for perc_down
    # index -> index
    def maxChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            #print('maxChild', self.heapList)
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # similar specification as perc_down, see class notes Normally these would be private but make them public
    # for testing purposes.
    # index -> index
    def perc_up(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def __repr__(self):
        return 'Capacity: {}, Current Size: {}, List: {}'.format(self.capacity, self.currentSize, self.heapList)

# takes a list of integers and returns a list containing the integers in non-decreasing order using the Heap Sort
# algorithm as described in class. Since your MaxHeap class is a max heap using the list internal to the heap to
# store the sorted elements will result in them being sorted in increasing order. This enables the reuse of the
# space but will destroy the heap order property. However, then you can just return the appropriate part of the
# internal list since you will not be using the heap anymore.
def heap_sort_increase(alist):
    h = MaxHeap(len(alist))
    h.build_heap(alist)
    sortedList = []
    while h.currentSize > 0:
        tmp = h.del_max()
        sortedList = [tmp] + sortedList
    return sortedList