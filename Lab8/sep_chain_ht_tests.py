# Terence Tong
# CSC 202 - 9
import unittest
from sep_chain_ht import *
import random

class MyTestCase(unittest.TestCase):
    def test_insert01(self):
        table = MyHashTable()
        for i in range(12):
            table.insert(i, i)
        self.assertEqual(table.hash_table[0], [(0, 0), (11, 11)])

    def test_insert02(self):
        table = MyHashTable()
        for i in range(17):
            table.insert(i, i)
        table.insert(18, 18)
        self.assertEqual(table.hash_table[0], [(0, 0)])

    def test_insert03(self):
        table = MyHashTable()
        table.insert(stringKey('d'), 'd')
        table.insert(stringKey('a'), 'a')
        table.insert(stringKey('abc'), 'abc')
        table.insert(stringKey('f'), 'f')
        table.insert(stringKey('as'), 'as')
        table.insert(stringKey('fg'), 'fg')
        table.insert(stringKey('gh'), 'gh')
        table.insert(stringKey('ki'), 'ki')
        table.insert(stringKey('cat'), 'cat')
        table.insert(stringKey('dog'), 'dog')
        table.insert(stringKey('dur'), 'dur')
        table.insert(stringKey('asdf'), 'asdf')
        table.insert(stringKey('dasdur'), 'dasdur')
        table.insert(stringKey('qwe'), 'qwe')
        table.insert(stringKey('rew'), 'rew')
        table.insert(stringKey('wrq'), 'wrq')
        table.insert(stringKey('tre'), 'tre')
        table.insert(stringKey('tyt'), 'tyt')
        table.insert(stringKey('ytr'), 'ytr')
        self.assertEqual(23, len(table.hash_table))

    def test_get01(self):
        table = MyHashTable()
        table.insert(stringKey('d'), 'd')
        table.insert(stringKey('a'), 'a')
        table.insert(stringKey('abc'), 'abc')
        table.insert(stringKey('f'), 'f')
        table.insert(stringKey('as'), 'as')
        table.insert(stringKey('fg'), 'fg')
        table.insert(stringKey('gh'), 'gh')
        table.insert(stringKey('ki'), 'ki')
        table.insert(stringKey('cat'), 'cat')
        table.insert(stringKey('dog'), 'dog')
        table.insert(stringKey('dur'), 'dur')
        self.assertEqual(table.get(ord('d')), (ord('d'), 'd'))
        with self.assertRaises(LookupError):
            table.get(0)

    def test_remove01(self):
        table = MyHashTable()
        table.insert(stringKey('d'), 'd')
        table.insert(stringKey('a'), 'a')
        table.insert(stringKey('abc'), 'abc')
        table.insert(stringKey('f'), 'f')
        table.insert(stringKey('as'), 'as')
        table.insert(stringKey('fg'), 'fg')
        table.insert(stringKey('gh'), 'gh')
        table.insert(stringKey('ki'), 'ki')
        table.insert(stringKey('cat'), 'cat')
        table.insert(stringKey('dog'), 'dog')
        table.insert(stringKey('dur'), 'dur')
        self.assertEqual(table.remove(stringKey('cat')), (stringKey('cat'), 'cat'))
        with self.assertRaises(LookupError):
            table.get(stringKey('cat'))
        table = MyHashTable()
        with self.assertRaises(LookupError):
            table.remove(12)

    def test_size(self):
        table = MyHashTable()
        num = random.randint(0,100)
        for i in range(num):
            table.insert(i, i)
        self.assertEqual(table.size(), num)

    def test_loadFactor(self):
        table = MyHashTable()
        table.insert(1, 1)
        self.assertAlmostEqual(table.load_factor(), 1/11)
        for i in range(16):
            table.insert(i+2, i+2)
        self.assertAlmostEqual(table.load_factor(), 17/23)

    def test_collisions(self):
        table = MyHashTable()
        for i in range(12):
            table.insert(i, i)
        self.assertEqual(table.collisions(), 1)
        table = MyHashTable()
        for i in range(12):
            table.insert(11*i, i)
        self.assertEqual(table.collisions(), 11)
        table = MyHashTable()
        self.assertEqual(table.collisions(), 0)


def stringKey(str):
    num = 0
    for i in str:
        num += ord(i)
    return num



if __name__ == '__main__':
    unittest.main()
