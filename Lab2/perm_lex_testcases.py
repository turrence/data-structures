'''
Name: Terence Tong
Section: 202 - 9
'''
from perm_lex import *

import unittest

class TestCase(unittest.TestCase): #is a unittest.TestCase
	#tests for 2 characters and 3 characters strings
	def test_permlex(self):
		self.assertEqual(perm_gen_lex("ab"), ["ab", "ba"])
		self.assertEqual(perm_gen_lex("abc"), ["abc", "acb", "bac", "bca", "cab", "cba"])
	
	#tests for 1 character
	def test_basecase(self):
		self.assertEqual(perm_gen_lex("a"), ["a"])
		
	#tests for empty strings	
	def test_emptyString(self):
		self.assertEqual(perm_gen_lex(""), [])
		
		
if(__name__ == '__main__'):
	unittest.main()