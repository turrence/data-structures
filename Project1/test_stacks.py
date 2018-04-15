''' 
Name: Terence Tong
Section: 202 - 9
'''
from stacks import *

import unittest

class TestCase(unittest.TestCase):
	#stackArray method tests
	def test_array_is(self):
		stack = StackArray(3)
		for i in range(3):
			stack.push(i)
		self.assertTrue(stack.is_full())
		self.assertFalse(stack.is_empty())
		for i in range(3): #executes 3 times but starts at 0 and ends at 2
			stack.pop()
		self.assertTrue(stack.is_empty())
		self.assertFalse(stack.is_full())
	
	def test_array_pushpop(self):
		stack = StackArray(3)
		for i in range(3):
			stack.push(i)	
		self.assertEqual(stack.items, [0, 1, 2])
		with self.assertRaises(IndexError):
			stack.push(3)
		for i in range(3): #executes 3 times but starts at 0 and ends at 2
			stack.pop()
		with self.assertRaises(IndexError):
			stack.pop()

	def test_array_peeksize(self):
		stack = StackArray(3)
		for i in range(3):
			stack.push(i)
		self.assertEqual(stack.peek(), 2)
		self.assertEqual(stack.size(), 3)
		for i in range(3):
			self.assertEqual(stack.peek(), 2-i)
			self.assertEqual(stack.size(), 3-i)
			stack.pop()
	
	#linked stack list tests
	def test_linked_is(self):
		linked = StackLinked(3)
		for i in range(3):
			node = Node(i)
			linked.push(node)
		self.assertTrue(linked.is_full())
		self.assertFalse(linked.is_empty())
		
	def test_linked_pushpop(self):
		linked = StackLinked(3)
		for i in range(3):
			node = Node(i)
			linked.push(node)
		with self.assertRaises(IndexError):
			linked.push(Node(3))
		self.assertEqual(linked.items.getData(), 2)
		self.assertEqual(linked.items.getNext().getData(), 1)
		linked.pop()
		self.assertEqual(linked.items.getData(), 1)
		linked.pop()
		self.assertEqual(linked.items.getData(), 0)
		linked.pop()
		self.assertTrue(linked.is_empty())
		with self.assertRaises(IndexError):
			linked.pop()
		
	def test_linked_peeksize(self):
		linked = StackLinked(3)
		for i in range(3):
			node = Node(i)
			linked.push(node)
		self.assertEqual(linked.peek(), linked.items)
		self.assertEqual(linked.size(), 3)
		for i in range(3):
			self.assertEqual(linked.size(), 3 - i)
			linked.pop()
		self.assertEqual(linked.peek(), None)	
'''
	def test_linked_nodeIslinked(self):
		node1 = Node(1)
		node2 = Node(2)
		node3 = Node(3)
		node1.setNext(node2)
		node2.setNext(node3)
		linked = StackLinked(3)
		linked.push(node1)
		self.assertEqual(linked.size(), 3)
		linked.pop()
		self.assertEqual(linked.items.getData(), 2)
		linked.pop()
		self.assertEqual(linked.items.getData(), 3)
		linked.pop()
		self.assertEqual(linked.items, None)
		linked.push(node1)
		with self.assertRaises(IndexError):
			linked.push(node3)
'''
if(__name__ == '__main__'):
	unittest.main()