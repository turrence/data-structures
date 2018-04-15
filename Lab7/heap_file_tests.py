import unittest

from heap_lab import *
import random


class MyTestCase(unittest.TestCase):
    def test_heap_insert1(self):
        heap = MaxHeap()
        heap.insert(2)
        heap.insert(3)
        heap.insert(5)
        heap.insert(6)
        heap.insert(9)
        self.assertEqual(heap.heapList[0], 0)
        self.assertEqual(heap.heapList[1], 9)
        self.assertEqual(heap.heapList[2], 6)
        self.assertEqual(heap.heapList[3], 3)
        self.assertEqual(heap.heapList[4], 2)
        self.assertEqual(heap.heapList[5], 5)

    def test_insert2(self):
        heap = MaxHeap()
        for i in range(50):
            heap.insert(i)
        self.assertFalse(heap.insert(51))

    def test_findmax1(self):
        heap = MaxHeap()
        alist = []
        for i in range(20):
            n = random.randint(0, 100)
            alist.append(n)
            self.assertTrue(heap.insert(n))
        self.assertTrue(heap.find_max(), max(alist))
        #print(heap)

    def test_findmax2(self):
        heap = MaxHeap()
        self.assertEqual(heap.find_max(), None)

    def test_delMax1(self):
        heap = MaxHeap()
        heap.insert(2)
        heap.insert(3)
        heap.insert(5)
        heap.insert(6)
        heap.insert(9)
        self.assertEqual(heap.del_max(), 9)
        self.assertEqual(heap.heapList[1], 6)
        #print('delmax1:', heap)
        heap = MaxHeap()
        heap.insert(9)
        heap.insert(14)
        heap.insert(11)
        heap.insert(17)
        heap.insert(18)
        heap.insert(19)
        heap.insert(21)
        heap.insert(33)
        heap.insert(27)
        self.assertEqual(heap.del_max(), 33)
        self.assertEqual(heap.heapList[1], 27)

    def test_delMax2(self):
        heap = MaxHeap()
        self.assertEqual(heap.del_max(), None)

    def test_buildHeap1(self):
        alist = [10,26,14,33,31,19,27,42,35,44]
        heap = MaxHeap()
        self.assertTrue(heap.build_heap(alist))
        #print(heap)
        self.assertEqual(heap.heapList[1], 44)
        self.assertEqual(heap.heapList[2], 42)
        self.assertEqual(heap.heapList[3], 27)
        self.assertEqual(heap.heapList[4], 35)
        self.assertEqual(heap.heapList[5], 31)
        self.assertEqual(heap.heapList[6], 19)
        self.assertEqual(heap.heapList[7], 14)
        self.assertEqual(heap.heapList[8], 33)
        self.assertEqual(heap.heapList[9], 10)
        self.assertEqual(heap.heapList[10], 26)

    def test_buildHeap2(self):
        alist = []
        for i in range(51):
            alist.append(i)
        heap = MaxHeap()
        self.assertFalse(heap.build_heap(alist))

    def test_isEmpty(self):
        heap = MaxHeap()
        self.assertTrue(heap.is_empty())
        heap.insert(1)
        self.assertFalse(heap.is_empty())

    def test_isFull(self):
        heap = MaxHeap(1)
        self.assertFalse(heap.is_full())
        heap.insert(1)
        self.assertTrue(heap.is_full())

    def test_heapCap(self):
        heap = MaxHeap()
        self.assertEqual(heap.get_heap_cap(), 50)
        heap = MaxHeap(1)
        self.assertEqual(heap.get_heap_cap(), 1)

    def test_heapSize(self):
        heap = MaxHeap()
        num = random.randint(0, 15)
        for i in range(num):
            heap.insert(i)
        self.assertEqual(heap.get_heap_size(), num)

    def test_percUP(self):
        heap = MaxHeap()
        list = [0, 7, 8, 6]
        heap.heapList = list
        heap.currentSize = 3
        heap.perc_up(2)
        self.assertEqual(heap.heapList[1], 8)
        self.assertEqual(heap.heapList[2], 7)
        self.assertEqual(heap.heapList[3], 6)
        list = [0, 7, 8, 6,4,12]
        heap.heapList = list
        heap.currentSize = 6
        heap.perc_up(5)
        self.assertEqual(heap.heapList[1], 12)
        self.assertEqual(heap.heapList[2], 7)
        self.assertEqual(heap.heapList[3], 6)
        self.assertEqual(heap.heapList[4], 4)
        self.assertEqual(heap.heapList[5], 8)

    def test_perc_down(self):
        heap = MaxHeap()
        list = [0, 3, 5, 12]
        heap.heapList = list
        heap.currentSize = 3
        heap.perc_down(1)
        self.assertEqual(heap.heapList[1], 12)
        self.assertEqual(heap.heapList[2], 5)
        self.assertEqual(heap.heapList[3], 3)
        list = [0, 12, 5, 3, 6, 7]
        heap.heapList = list
        heap.currentSize = 6
        heap.perc_down(2)
        self.assertEqual(heap.heapList[2], 7)
        self.assertEqual(heap.heapList[4], 6)
        self.assertEqual(heap.heapList[5], 5)

    def test_heap_sort(self):
        l = [8, 4, 7, 1, 3, 5]
        self.assertEqual(heap_sort_increase(l), [1,3,4,5,7,8])
        l = []
        for i in range(500):
            l.append(random.randint(0,100))
        self.assertEqual(heap_sort_increase(l), sorted(l))
        l = [1]
        self.assertEqual(heap_sort_increase(l), l)


if __name__ == '__main__':
    unittest.main()
