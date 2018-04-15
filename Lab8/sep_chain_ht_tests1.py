import unittest
from sep_chain_ht import *

# test cases
class sep_chain_ht_tests(unittest.TestCase):
    def test_insert(self):
        h = MyHashTable(3)
        h.insert(2, 'c')
        h.insert(8, 'a')
        h.insert(3, 't')
        h.insert(5, 'd')
        # before resizing
        self.assertEqual(h.hash_table, [[(3, 't')], [], [(2, 'c'), (8, 'a'), (5, 'd')]])
        self.assertEqual(h.size(), 4)
        self.assertEqual(h.collisions(),2)
        h.insert(6, 's')
        # now table size is 7 and rehash everything reading it from the table
        self.assertEqual(h.hash_table, [[], [(8, 'a')], [(2, 'c')], [(3, 't'), ], [], [(5, 'd')], [(6, 's')]])
        self.assertEqual(h.size(), 5)
        self.assertEqual(h.collisions(), 0)
        h.insert(2, 'f')
        self.assertEqual(h.hash_table, [[], [(8, 'a')], [(2, 'f')], [(3, 't'), ], [], [(5, 'd')], [(6, 's')]])
        self.assertEqual(h.size(), 5)
        self.assertEqual(h.collisions(), 0)

    def test_remove(self):
        h = MyHashTable(3)
        h.insert(2, 'c')
        h.insert(8, 'a')
        h.insert(3, 't')
        h.insert(5, 'd')
        h.insert(6, 's')
        h.insert(2, 'f')
        self.assertEqual(h.remove(6),(6, 's'))
        self.assertEqual(h.size(),4)
        self.assertEqual(h.remove(2),(2, 'f'))
        self.assertEqual(h.size(),3)
        a = MyHashTable(3)
        a.insert(2, 'c')
        a.insert(8, 'a')
        a.insert(3, 't')
        a.insert(5, 'd')
        self.assertEqual(a.remove(5), (5, 'd'))
        self.assertEqual(a.size(), 3)
        self.assertEqual(a.collisions(),1)
        b = MyHashTable(3)
        b.insert(2, 'c')
        b.insert(8, 'a')
        b.insert(3, 't')
        b.insert(5, 'd')
        with self.assertRaises(LookupError):
            b.remove(14)

    def test_get(self):
        h = MyHashTable(3)
        h.insert(2, 'c')
        h.insert(8, 'a')
        h.insert(3, 't')
        h.insert(5, 'd')
        self.assertEqual(h.get(3),(3, 't'))
        with self.assertRaises(LookupError):
            h.get(14)
        with self.assertRaises(LookupError):
            h.get(1)

    def test_load_factor(self):
        h = MyHashTable(2)
        h.insert(2, 'c')
        h.insert(8, 'a')
        h.insert(3, 't')
        self.assertAlmostEqual(h.load_factor(), 1.5)
        h.insert(5, 'd')
        self.assertAlmostEqual(h.load_factor(), 0.8)
        h.insert(6, 'f')
        self.assertAlmostEqual(h.load_factor(),1)

    def test_size(self):
        h = MyHashTable(3)
        h.insert(2, 'c')
        h.insert(8, 'a')
        h.insert(3, 't')
        h.insert(5, 'd')
        h.insert(6, 's')
        h.insert(2, 'f')
        self.assertEqual(h.size(),5)

    def test_collisions(self):
        h = MyHashTable(3)
        h.insert(2, 'c')
        h.insert(8, 'a')
        h.insert(3, 't')
        h.insert(5, 'd')
        self.assertEqual(h.collisions(),2)
        h.insert(6, 's')
        h.insert(2, 'f')
        self.assertEqual(h.collisions(),0)


if __name__ == "__main__":
    unittest.main()
