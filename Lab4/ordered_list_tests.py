"""
Name: Martin Jiang and Terence Tong
Class: 202 - 9
"""

import unittest
from ordered_list import *

class MyTestCase(unittest.TestCase):
    def test_orderedlist_add(self):
        list = OrderedList()
        list.add(10)
        list.add(4)
        list.add(12)
        list.add(3)
        self.assertEqual(list.head.data, 3)
        self.assertEqual(list.head.next.data, 4)
        self.assertEqual(list.head.next.next.data, 10)
        self.assertEqual(list.head.next.next.next.data, 12)
        self.assertEqual(list.head.next.next.next.next, None)
        self.assertEqual(list.tail.prev.data, 10)
        self.assertEqual(list.tail.data, 12)

    def test_orderedlist_remove(self):
        list = OrderedList()
        list.add(10)
        list.add(4)
        list.add(12)
        list.add(3)
        self.assertEqual(list.remove(13), -1)
        self.assertEqual(list.remove(12), 3)
        list.add(12)
        self.assertEqual(list.remove(3), 0)
        list.add(3)
        self.assertEqual(list.remove(4), 1)
        list.add(4)
        self.assertEqual(list.remove(5), -1)
        self.assertEqual(list.remove(0), -1)
        list.remove(10)
        list.remove(4)
        list.remove(12)
        list.remove(3)
        self.assertEqual(list.remove(1), -1)

    def test_orderedList_searchBack(self):
        list = OrderedList()
        list.add(10)
        list.add(4)
        list.add(12)
        list.add(3)
        self.assertTrue(list.search_backwards(3))
        self.assertFalse(list.search_backwards(0))
        self.assertFalse(list.search_backwards(5))
        self.assertFalse(list.search_backwards(13))
        self.assertTrue(list.search_backwards(12))
        list1 = OrderedList()
        self.assertFalse(list1.search_backwards(2))

    def test_OrderedList_searchFor(self):
        list = OrderedList()
        list.add(10)
        list.add(4)
        list.add(12)
        list.add(3)
        self.assertTrue(list.search_forward(3))  # tests to see if search_forward returns true when value is in list
        list.pop(0)
        self.assertFalse(
            list.search_forward(3))  # tests to see if search_forward returns False when value is popped from list
        self.assertFalse(
            list.search_forward(13))  # tests to see if search_forward returns False when value isn't in list
        self.assertFalse(
            list.search_forward(14))  # tests to see if search_forward returns False when value isn't in list
        self.assertFalse(
            list.search_forward(0))  # tests to see if search_forward returns False when value isn't in list
        self.assertTrue(list.search_forward(12))  # tests to see if search_forward returns True when value is in list
        list1 = OrderedList()
        self.assertFalse(list1.search_forward(1))

    def test_OrderedList_is_empty(self):
        list = OrderedList()
        self.assertTrue(list.is_empty())  # tests to see if is_empty returns True when list is empty
        list.add(1)
        self.assertFalse(list.is_empty())  # tests to see if is_empty returns False when list has a value
        list.pop()
        self.assertTrue(list.is_empty())  # tests to see if is_empty returns True after pop of last value

    def test_OrderedList_index(self):
        list = OrderedList()
        list.add(10)
        list.add(4)
        list.add(12)
        list.add(3)
        self.assertEqual(list.index(3), 0)  # tests to see if index returns 0 for first item
        self.assertEqual(list.index(30),
                         -1)  # tests to see if index returns -1 if item isn't in list and is greater than tail
        self.assertEqual(list.index(12), 3)  # tests to see if index returns size - 1 for last item in list
        self.assertEqual(list.index(-1),
                         -1)  # tests to see if index returns -2 if item isn't in list and is less than head

    def test_OrderedLIst_pop(self):
        list = OrderedList()
        list.add(10)
        self.assertEqual(list.pop(), 10)  # tests to see if pop returns 10 when list is only one item
        list.add(4)
        list.add(12)
        list.add(3)
        self.assertEqual(list.pop(0), 3)  # tests to see if pop returns first if index is 0
        list.add(10)
        self.assertEqual(list.pop(2), 12)  # tests to see if pop returns last item if index is size-1
        list2 = OrderedList()
        list2.add(2)
        list2.add(13)
        list2.add(20)
        list2.add(24)
        list2.add(36)
        list2.add(40)
        self.assertEqual(list2.pop(4), 36)  # tests to see if pop returns correct value when pos > (size/2)
        self.assertEqual(list2.pop(2), 20)  # tests to see if pop returns correct value when pos < (size/2)
        self.assertEqual(list2.pop(2), 24)  # tests to see if pop returns correct value when pos == (size/2)
        with self.assertRaises(IndexError):
            list = OrderedList()
            list.pop()

if __name__ == '__main__':
    unittest.main()
