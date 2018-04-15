import unittest
from heap_lab import *


class Tests_Heaps(unittest.TestCase):
    def test_find_max(self):
        list = [0, 3, 6, 5, 2, 9]
        h = MaxHeap(50)
        heap = h.build_heap(list)
        self.assertEqual(h.find_max(), 9)

    def test_insert(self):
        h = MaxHeap(50)
        h.insert(4)
        h.insert(90)
        h.insert(-2)
        h.insert(22)
        h.insert(8)
        self.assertEqual(h.heap_contents(), [90, 22, -2, 4, 8])
        a = MaxHeap(3)
        a.insert(4)
        a.insert(90)
        a.insert(-2)
        self.assertEqual(a.insert(2), False)

    def test_del_max(self):
        h = MaxHeap(50)
        h.insert(4)
        self.assertTrue(h.insert(90))
        h.insert(-2)
        h.insert(22)
        h.insert(8)
        h.del_max()
        self.assertEqual(h.heap_contents(), [22, 8, -2, 4])
        h.del_max()
        self.assertEqual(h.heap_contents(), [8, 4, -2])
        a = MaxHeap(3)
        self.assertEqual(a.del_max(), None)

    def test_heap_contents(self):
        h = MaxHeap(50)
        h.insert(4)
        h.insert(90)
        h.insert(-2)
        h.insert(22)
        h.insert(8)
        self.assertEqual(h.heap_contents(), [90, 22, -2, 4, 8])
        a = MaxHeap(3)
        self.assertEqual(a.heap_contents(),[])
        a.insert(4)
        a.insert(90)
        a.insert(-2)
        self.assertFalse(a.insert(1))

    def test_build_heap(self):
        list = [13, 19, 68, 14, 21, 17, 65, 26, 32, 31]
        h = MaxHeap(13)
        h.build_heap(list)
        self.assertEqual(h.heap_contents(), [68, 32, 65, 26, 31, 17, 13, 19, 14, 21])
        list = []
        self.assertTrue(h.build_heap(list))
        self.assertEqual(h.heap_contents(),[])
        a = MaxHeap(3)
        list = [1,2,3,4,-1]
        self.assertFalse(a.build_heap(list))

    def test_is_empty(self):
        h = MaxHeap(10)
        self.assertTrue(h.is_empty())
        h.insert(10)
        self.assertFalse(h.is_empty())

    def test_is_full(self):
        h = MaxHeap(3)
        self.assertFalse(h.is_full())
        h.insert(10)
        h.insert(12)
        h.insert(14)
        self.assertTrue(h.is_full())

    def test_get_heap_cap(self):
        h = MaxHeap(40)
        self.assertEqual(h.get_heap_cap(), 40)
        a = MaxHeap(30)
        self.assertEqual(a.get_heap_cap(), 30)

    def test_get_heap_size(self):
        h = MaxHeap(3)
        h.insert(4)
        h.insert(90)
        self.assertEqual(h.get_heap_size(), 2)

    def test_heap_sort_increase(self):
        h = MaxHeap(50)
        list = [4,8,29,90,-2,1,11]
        h.build_heap(list)
        self.assertEqual(h.heap_contents(),[90,8,29,4,-2,1,11])
        self.assertEqual(heap_sort_increase(list),[-2,1,4,8,11,29,90] )
        list = [-2]
        self.assertEqual(heap_sort_increase(list),[-2])

if __name__ == "__main__":
    unittest.main()
