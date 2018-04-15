import unittest
from queues import *


# various test cases for all the function written for the queue.py file
class TestCase(unittest.TestCase):
    # test cases for each function of the QueueArray Class
    def test__QueueArrayis_empty(self):
        s = QueueArray(2)
        self.assertEqual(s.is_empty(), True)
        s.enqueue(3)
        s.enqueue(4)
        self.assertEqual(s.is_empty(), False)
        s.dequeue()
        s.dequeue()
        self.assertEqual(s.is_empty(), True)

    def test_QueueArray_is_full(self):
        s = QueueArray(3)
        self.assertEqual(s.is_full(), False)
        s.enqueue(2)
        s.enqueue(3)
        s.enqueue(1)
        self.assertEqual(s.is_full(), True)
        s.dequeue()
        s.dequeue()
        s.dequeue()
        self.assertEqual(s.is_full(), False)

        t = QueueArray(4)
        t.enqueue(1)
        t.enqueue(2)
        t.enqueue(3)
        t.dequeue()
        self.assertEqual(t.is_full(), False)
        t.enqueue(3)
        t.enqueue(2)
        self.assertEqual(t.is_full(), True)

    def test_QueueArray_enqueue(self):
        s = QueueArray(3)
        s.enqueue(1)
        self.assertEqual(s.items, [1, None, None])
        s.enqueue(3)
        s.enqueue(4)
        self.assertEqual(s.items, [1, 3, 4])
        with self.assertRaises(IndexError):
            s.enqueue(1)
        s.dequeue()
        s.dequeue()
        self.assertEqual(s.items, [None, None, 4])
        s.enqueue(2)
        self.assertEqual(s.items, [2, None, 4])

        t = QueueArray(6)
        t.enqueue(1)
        t.enqueue(2)
        t.enqueue(3)
        t.dequeue()
        t.enqueue(4)
        t.enqueue(2)
        t.enqueue(3)
        t.dequeue()
        t.dequeue()
        self.assertEqual(t.items, [None, None, None, 4, 2, 3])

    def test_QueueArray_dequeue(self):
        s = QueueArray(3)
        s.enqueue(1)
        s.enqueue(3)
        s.enqueue(4)
        self.assertEqual(s.dequeue(), 1)
        self.assertEqual(s.dequeue(), 3)
        self.assertEqual(s.dequeue(), 4)
        with self.assertRaises(IndexError):
            s.dequeue()
        s.enqueue(1)
        s.enqueue(3)
        s.enqueue(4)
        s.dequeue()
        s.enqueue(2)
        self.assertEqual(s.items, [2, 3, 4])
        s.dequeue()
        self.assertEqual(s.items, [2, None, 4])

    def test_QueueArray_num_in_queue(self):
        s = QueueArray(3)
        s.enqueue(1)
        s.enqueue(3)
        s.enqueue(4)
        self.assertEqual(s.num_in_queue(), 3)
        s.dequeue()
        self.assertEqual(s.num_in_queue(), 2)
        s.dequeue()
        s.dequeue()
        self.assertEqual(s.num_in_queue(), 0)
        s.enqueue(4)
        self.assertEqual(s.num_in_queue(), 1)

    # test cases for each function in the QueueLinked class
    def test_QueueLinked_is_empty(self):
        s = QueueLinked(3)
        self.assertEqual(s.is_empty(), True)
        s.enqueue(2)
        s.enqueue(4)
        s.enqueue(3)
        self.assertEqual(s.is_empty(), False)

    def test_QueueLinked_is_full(self):
        s = QueueLinked(3)
        self.assertEqual(s.is_full(), False)
        s.enqueue(2)
        s.enqueue(4)
        s.enqueue(3)
        self.assertEqual(s.is_full(), True)
        s.dequeue()
        self.assertEqual(s.is_full(), False)

    def test_QueueLinked_enqueue(self):
        s = QueueLinked(3)
        s.enqueue(3)
        self.assertEqual(s.front.data, 3)
        self.assertEqual(s.rear.data, 3)
        s.enqueue(2)
        s.enqueue(5)
        self.assertEqual(s.front.data, 3)
        self.assertEqual(s.rear.data, 5)
        with self.assertRaises(IndexError):
            s.enqueue(1)
        t = QueueLinked(0)
        with self.assertRaises(IndexError):
            s.enqueue(1)

    def test_QeueueLinked_dequeue(self):
        s = QueueLinked(3)
        s.enqueue(3)
        s.enqueue(2)
        s.enqueue(5)
        self.assertEqual(s.dequeue(), 3)
        self.assertEqual(s.dequeue(), 2)
        self.assertEqual(s.dequeue(), 5)
        with self.assertRaises(IndexError):
            s.dequeue()

    def test_QueueLinked_num_in_queue(self):
        s = QueueLinked(3)
        s.enqueue(3)
        s.enqueue(2)
        s.enqueue(5)
        self.assertEqual(s.num_in_queue(), 3)
        s.dequeue()
        self.assertEqual(s.num_in_queue(), 2)
        s.dequeue()
        s.dequeue()
        self.assertEqual(s.num_in_queue(), 0)


# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()
