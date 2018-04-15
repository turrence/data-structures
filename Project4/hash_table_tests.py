import unittest
from hash_lin_table import *
from hash_quad_table import *


class MyTestCase(unittest.TestCase):
    def test_line_table(self):
        t = HashTableLinPr(10)
        # anagrams so all should have same hash Value
        t.insert_word('abets', 0)
        # print(t.myhash('abets', 10))
        t.insert_word('baste', 0)
        # print(t.myhash('baste', 10))
        t.insert_word('betas', 0)
        # print(t.myhash('betas', 10))
        t.insert_word('beast', 0)
        # print(t.myhash('beast', 10))
        t.insert_word('beats', 0)
        # print(t.myhash('beats', 10))
        self.assertEqual(t.hash_table[2], ('abets', [0]))
        self.assertEqual(t.hash_table[3], ('baste', [0]))
        self.assertEqual(t.hash_table[4], ('betas', [0]))
        self.assertEqual(t.hash_table[5], ('beast', [0]))
        self.assertEqual(t.hash_table[6], ('beats', [0]))
        t.insert_word('beats', 10)
        self.assertEqual(t.hash_table[6], ('beats', [0, 10]))

    def test_quad_table(self):
        t = HashTableQuadPr(10)
        # anagrams so all should have same hash Value
        t.insert_word('abets', 0)
        # print(t.myhash('abets', 10))
        t.insert_word('baste', 0)
        # print(t.myhash('baste', 10))
        t.insert_word('betas', 0)
        # print(t.myhash('betas', 10))
        t.insert_word('beast', 0)
        # print(t.myhash('beast', 10))
        t.insert_word('beats', 0)
        # print(t.myhash('beats', 10))
        self.assertEqual(t.hash_table[2], ('abets', [0]))
        self.assertEqual(t.hash_table[3], ('baste', [0]))
        self.assertEqual(t.hash_table[6], ('betas', [0]))
        self.assertEqual(t.hash_table[1], ('beast', [0]))
        self.assertEqual(t.hash_table[8], ('beats', [0]))
        t.insert_word('beats', 12)
        self.assertEqual(t.hash_table[8], ('beats', [0, 12]))

    def test_rehash(self):
        t= HashTableLinPr(7)
        t.insert_word('lapse', 0)
        t.insert_word('leaps', 0)
        t.insert_word('pales', 0)
        t.insert_word('peals', 0)
        t.insert_word('pleas', 0)
        t.insert_word('sepal', 0)
        self.assertEqual(len(t.hash_table), 15)
        self.assertEqual(t.num_items, 6)



if __name__ == '__main__':
    unittest.main()
