import unittest
from queues import *

class MyTestCase(unittest.TestCase):
    def test_array_queue(self):
        qarr = QueueArray(5)
        qarr.enqueue(1)
        qarr.enqueue(2)
        qarr.enqueue(3)
        qarr.enqueue(4)
        qarr.enqueue(5)
        self.assertTrue(qarr.is_full())
        self.assertEqual(qarr.dequeue(), 1)
        self.assertEqual(qarr.dequeue(), 2)
        self.assertEqual(qarr.dequeue(), 3)
        self.assertEqual(qarr.dequeue(), 4)
        self.assertEqual(qarr.dequeue(), 5)
        self.assertTrue(qarr.is_empty())

    def test_circular_array(self):
        qArr = QueueArray(3)
        qArr.enqueue(1)
        qArr.enqueue(2)
        qArr.enqueue(3)
        self.assertEqual(qArr.dequeue(), 1)
        qArr.enqueue(1)
        self.assertEqual(qArr.dequeue(), 2)
        qArr.enqueue(4)
        with self.assertRaises(IndexError):
            qArr.enqueue(4)
        for i in range(3):
            qArr.dequeue()
        with self.assertRaises(IndexError):
            qArr.dequeue()
        self.assertEqual(qArr.num_in_queue(), 0)

    def test_queue_linked(self):
        qLink = QueueLinked(3)
        qLink.enqueue(1)
        qLink.enqueue(2)
        qLink.enqueue(3)
        self.assertTrue(qLink.is_full())
        self.assertEqual(qLink.dequeue(), 1)
        self.assertEqual(qLink.dequeue(), 2)
        self.assertEqual(qLink.dequeue(), 3)
        self.assertEqual(qLink.num_in_queue(), 0)
        qLink.enqueue(1)
        self.assertEqual(qLink.dequeue(),1)


if __name__ == '__main__':
    unittest.main()
