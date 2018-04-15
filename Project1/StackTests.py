import unittest
from  stacks import StackArray
from stacks import StackLinked


class TestStacksArray(unittest.TestCase):
    def test_push(self):
        stk_a = StackArray(10)
        stk_a.push(3)
        self.assertEqual(stk_a.peek(), 3 )
        self.assertEqual(stk_a.pop(), 3 )
        self.assertTrue(stk_a.is_empty())
    def test_pop(self): 
        stk_a = StackArray(4)
        with self.assertRaises(IndexError): 
            stk_a.pop()
        stk_a.push(6)
        stk_a.push(7)
        stk_a.push(9)
        self.assertEqual(stk_a.pop(), 9)
        self.assertEqual(stk_a.pop(), 7)
        self.assertEqual(stk_a.pop(), 6)
    def test_size(self):
        stk_a = StackArray(4)
        stk_a.push(6)
        stk_a.push(7)
        stk_a.push(8)
        stk_a.push(9)
        self.assertTrue(stk_a.is_full())
        with self.assertRaises(IndexError): 
            stk_a.push(0)
        self.assertEqual(stk_a.size(), 4 )
        self.assertEqual(stk_a.pop(), 9 )
        self.assertEqual(stk_a.size(), 3 )
        self.assertFalse(stk_a.is_empty())

class TestStacksLinked(unittest.TestCase):
    def test_push(self):
        stk_a = StackLinked(4)
        stk_a.push(3)
        self.assertEqual(stk_a.peek(), 3 )
        self.assertEqual(stk_a.pop(), 3 )
        self.assertTrue(stk_a.is_empty())
    def test_pop(self): 
        stk_a = StackArray(4)
        with self.assertRaises(IndexError): 
            stk_a.pop()
        stk_a.push(6)
        stk_a.push(7)
        stk_a.push(9)
        self.assertEqual(stk_a.pop(), 9)
        self.assertEqual(stk_a.pop(), 7)
        self.assertEqual(stk_a.pop(), 6)
    def test_size(self):
        stk_a = StackLinked(4)
        stk_a.push(6)
        stk_a.push(7)
        stk_a.push(8)
        stk_a.push(9)
        self.assertTrue(stk_a.is_full())
        with self.assertRaises(IndexError): 
            stk_a.push(0)
        self.assertEqual(stk_a.size(), 4 )
        self.assertEqual(stk_a.pop(), 9 )
        self.assertEqual(stk_a.size(), 3 )
        self.assertFalse(stk_a.is_empty())

        

if __name__ == "__main__":
    unittest.main()
