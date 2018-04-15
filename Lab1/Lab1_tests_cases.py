#Test Cases for Lab1
# Name: Terence Tong
# Section: CSC 202
from Lab1 import *

import unittest

class TestCase(unittest.TestCase):
	def test_max_list_iter(self):
		tlist = [10, 9, 8 ,4, 9]
		self.assertEqual(max_list_iter(tlist),10)
		tlist = []
		with self.assertRaises(ValueError):  # magic - uses context manager
			max_list_iter(tlist)

	def test_reverse_rec(self):
		self.assertEqual(reverse_rec("abcd"),"dcba")	
	
	#runs a binary search on an array with an even amount of elements; tests for targesa not in the list
	def test_even_bin_search(self):
		evenList = [0, 1, 2, 3, 4, 5]
		#out of bounds lower bound binary search
		self.assertEqual(bin_search(-10, 0, len(evenList)-1, evenList), None)
		#checks that all numbers match with their position
		for num in evenList:
			self.assertEqual(bin_search(num, 0, len(evenList)-1, evenList), num)
		#out of bounds upper bound binary search
		self.assertEqual(bin_search(10, 0, len(evenList) - 1, evenList), None)
	
	#runs a binary search on an array with an odd amount of elements; tests for targets not in the list
	def test_odd_bin_search(self):
		oddList = [0, 1, 2, 3, 4, 5, 6]
		#out of bounds lower bound binary search
		self.assertEqual(bin_search(-10, 0, len(oddList)-1, oddList), None)
		#checks that all numbers match with their position
		for num in oddList:
			self.assertEqual(bin_search(num, 0, len(oddList)-1, oddList), num)
		#out of bounds upper bound binary search
		self.assertEqual(bin_search(10, 0, len(oddList) - 1, oddList), None)
	
	#takes an unordered array and returns the index of the target of where it would have been if the array was sorted
	def test_unordered_arr_bin_search(self):
		unOrdered = [9, 5, 2, 5, 12, 7, 13]
		self.assertEqual(bin_search(2, 0, len(unOrdered) - 1, unOrdered), 0)
		self.assertEqual(bin_search(13, 0, len(unOrdered) - 1, unOrdered), len(unOrdered) - 1 )
		
	#number searched for is within the array but the low and high index does not include where the target is
	def test_in_arr_not_in_bounds(self):
		list = [0, 1, 2, 3, 4, 5]
		self.assertEqual(bin_search(0, 1, len(list)-1, list), None)
		
	#tests binary search on an empty array
	def test_empty_list_bin_search(self):
		list = []
		self.assertEqual(bin_search(10, 0, len(list)-1, list), None)
		
# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()
