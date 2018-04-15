#Terence Tong
#CSC 202 - 9
import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_invalid(self):
        self.assertFalse(postfix_valid(""))
        self.assertFalse(postfix_valid("2 3"))
 
    def test_valid(self):
        self.assertTrue(postfix_valid("2 3 +"))
        self.assertTrue(postfix_valid("2 3 -"))
        self.assertTrue(postfix_valid("2 3 *"))
        self.assertTrue(postfix_valid("2 3 /"))
        self.assertTrue(postfix_valid("2 -3 /"))


    def test_postfixeval1(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfixeval(self):
        self.assertAlmostEqual(postfix_eval("1.5 .5 - 3 * 7 + 10 -"), 0 )

    def test_postfixeval2(self):
        self.assertEqual(postfix_eval("12 10 2 * - 11 + 3 /"), 1)

    def test_inToPostBasicAssoc(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")

    def test_inToPostBasicAssoc1(self):
        self.assertEqual(infix_to_postfix("6 - 3 + 2"), "6 3 - 2 +")

    def test_inToPostBasicAssoc2(self):
        self.assertEqual(infix_to_postfix("6 ^ 3 ^ 2"), "6 3 2 ^ ^")

    def test_inToPostBasicAssoc3(self):
        self.assertEqual(infix_to_postfix("6 * ( 3 + 2 )"), "6 3 2 + *")
        self.assertEqual(infix_to_postfix("( 13 + 12 ) - ( ( 10 * 3 ) - 1 ) / 2"), "13 12 + 10 3 * 1 - 2 / -")
        self.assertEqual(infix_to_postfix("12.2 + 13 - 21 / 7"), "12.2 13 + 21 7 / -")
        self.assertEqual(infix_to_postfix("( 2 - 1 ) * 2 ^ 1 ^ 4 * 1"), "2 1 - 2 1 4 ^ ^ * 1 *")


    def test_inToPostBasicAssoc5(self):
        self.assertEqual(infix_to_postfix("6"), "6")
        with self.assertRaises(ValueError): 
            postfix_eval("3 0 /")

if __name__ == "__main__":
    unittest.main()
