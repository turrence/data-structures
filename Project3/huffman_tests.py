import unittest
import filecmp

from huffman import *


class TestList(unittest.TestCase):

    def test_cnt_freq(self):
        with self.assertRaises(IOError):
            cnt_freq('')
        freqlist = cnt_freq("file1.txt")
        anslist = [0]*256
        anslist[97:104] = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist[97:104])


    def test_create_huff_tree(self):
        freqlist = cnt_freq("file1.txt")
        hufftree = create_huff_tree(freqlist)
        numchars = 32
        charforroot = "a"
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_create_code(self):
        freqlist = cnt_freq("file1.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')


    def test_onechar_file(self):
        file = open('onechar.txt', 'w')
        file.truncate()
        file.write('a')
        file.close()
        file = open('testfile.txt', 'w')
        file.truncate()
        file.write('\'a\' 1')
        file.close()
        frlist = cnt_freq("onechar.txt")
        list = [0]*256
        list[ord('a')] = 1
        self.assertEqual(frlist, list)
        hufftree = create_huff_tree(frlist)
        create_code(hufftree)
        self.assertEqual(hufftree.char, ord('a'))
        self.assertEqual(hufftree.freq, 1)
        self.assertEqual(hufftree.code, '')
        huffman_encode('onechar.txt', 'onechar.txt')
        self.assertTrue(filecmp.cmp('onechar.txt', 'testfile.txt'))

    def test_empty_file(self):
        huffman_encode('empty.txt', 'encoded_empty.txt')
        self.assertTrue(filecmp.cmp('empty.txt', 'encoded_empty.txt'))


    def test_decode_empty_file(self):
        huffman_decode(['']*256, 'empty.txt', 'encoded_empty.txt')
        self.assertTrue(filecmp.cmp('empty.txt', 'encoded_empty.txt'))

    def test_nonexisting_file(self):
        with self.assertRaises(IOError):
            cnt_freq("notthere.txt")

    def test_01_encodefile(self):
        huffman_encode("file1.txt", "output1.txt")
        # capture errors by running 'filecmp' on your encoded file
        # with a *known* solution file
        self.assertTrue(filecmp.cmp("output1.txt", "output1_soln.txt"))

    def test_01_decodefile(self):
        freqlist = cnt_freq("file1.txt")
        huffman_decode(freqlist,"output1.txt", "decodefile1.txt")
        # capture errors by running 'filecmp' on your encoded file
        # with a *known* solution file
        self.assertTrue(filecmp.cmp("decodefile1.txt", "file1.txt"))

    def test_more_char(self):
        huffman_decode(cnt_freq('morechar.txt'), 'encoded_morechar.txt', 'testfile.txt')
        self.assertTrue(filecmp.cmp('morechar.txt', 'testfile.txt'))

  # tests when there are just one character multiple times
    def test_one_char(self):
        file = open("onechar.txt", 'w')
        file.truncate()
        file.write('aaaaaaaaaaaaaaaaaaaaa')  # 21 a's
        file.close()
        file = open('testfile.txt', 'w')
        file.truncate()
        file.write('\'a\' 21')
        file.close()
        huffman_encode('onechar.txt', 'encoded_onechar.txt')
        self.assertTrue(filecmp.cmp('encoded_onechar.txt', 'testfile.txt'))



if __name__ == '__main__': 
    unittest.main()
