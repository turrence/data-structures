# Name: Terence Tong
# Section: 202 - 9

# an implementation of Huffman Nodes to encode text files A BINARY TREE
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = ord(char) if not isinstance(char, int) else char # actually the character code
        self.freq = freq
        self.code = None
        self.left = None
        self.right = None

    def __repr__(self):
        return 'HuffmanNode(Char: {}, Freq: {}, L: {}, R: {})'.format(chr(self.char), self.freq, self.left, self.right)


# HELPER
# finds the node that comes_before() all other nodes
# also deletes the found node from list
# list of huffmanNode -> huffmannode
def find_min_node(nodeList):
    minNode = nodeList[0]
    for i in range(len(nodeList)):
        if comes_before(nodeList[i], minNode):
            minNode = nodeList[i]
    nodeList.remove(minNode)
    return minNode


# HELPER
# creates a list of huffmanNodes based off character frequency and index
# list of ints -> Huffman node List
def create_huffman_list(char_freq):
    if char_freq is None:
        return None
    huffList = []
    for i in range(len(char_freq)):
        if char_freq[i] != 0:
            huffList.append(HuffmanNode(chr(i), char_freq[i]))
    i = 1
    while i < len(huffList):
        j = i
        while j > 0 and not comes_before(huffList[j-1], huffList[j]):
            temp = huffList[j]
            huffList[j] = huffList[j-1]
            huffList[j-1] = temp
            j -= 1
        i += 1
    return huffList


# HELPER
# recursive function that does create_code
# HuffmanNode, string, list -> None
def creating_code(node, stringCode, codeList):
    if node is None:
        return
    temp = stringCode
    if node.left is None and node.right is None:
        codeList[node.char] = stringCode
        node.code = stringCode
    if node.left is not None:
        stringCode += '0'
        creating_code(node.left, stringCode, codeList)
    if node.right is not None:
        temp += '1'
        creating_code(node.right, temp, codeList)


# PART A
# returns true if tree rooted at node a comes before tree rooted at node b
# HuffmanNode, HuffmanNode -> boolean
def comes_before(a, b):
    if a.freq < b.freq:
        return True
    elif a.freq == b.freq:
        if a.char < b.char:
            return True
    return False


# PART A
#  text file -> list of frequencies of characters
def cnt_freq(filename):
    freqList = [0] * 256
    try:
        text = open(filename, 'r', encoding='utf-8-sig')
    except FileNotFoundError:
        raise IOError
    for line in text:
        for char in line:
            freqList[ord(char)] += 1
    text.close()
    if max(freqList) == 0:
        return None
    return freqList


# PART A
# takes a list of ints -> HuffmanTree root node
def create_huff_tree(char_freq):
    huffList = create_huffman_list(char_freq)
    if huffList is None:
        return None
    while len(huffList) > 1:
        min1 = find_min_node(huffList)
        min2 = find_min_node(huffList)
        node = HuffmanNode(min1.char if min1.char < min2.char else min2.char, min1.freq + min2.freq)
        node.left = min1
        node.right = min2
        #print(min1)
        #print(min2)
        #print(node)
        index = 0
        while index < len(huffList) and not comes_before(node, huffList[index]):
            index += 1
        huffList.insert(index, node)
    return huffList[0]


# PART A
# creates a list with each character corresponding to its code
# huffmanNode (should the root) -> list of codes
def create_code(node):
    codeList = ['']*256
    creating_code(node, '', codeList)
    return codeList


# PART B
# gets text from the first file and writes the encoded text to the out_file
# 2 files -> None
def huffman_encode(in_file, out_file):
    try:
        codeList = create_code(create_huff_tree(cnt_freq(in_file)))
    except FileNotFoundError:
        raise IOError
    if cnt_freq(in_file) is None:  # checks if in_file was empty
        file = open(out_file, 'w')
        file.truncate()
        file.close()
        return
    text = ''
    counter = 0
    character = ''
    file = open(in_file, 'r', encoding='utf-8-sig')
    for line in file:
        for char in line:
            text += codeList[ord(char)]
            counter += 1
            character = char
    if text == '':
        text = '\'{}\' {}'.format(character, counter)
    file.close()
    outFile = open(out_file, 'w')
    outFile.truncate()
    outFile.write(text)
    outFile.close()


# PART B
# creates a tree from the freqs to make a code to translate the encoded_file and writes translated to decode_file
# list of ints, file, file -> None
def huffman_decode(freqs, encoded_file, decode_file):
    tree = create_huff_tree(freqs)
    if tree is None:
        file = open(decode_file, 'w')
        file.truncate()
        file.close()
    faketree = tree
    text = ''
    try:
        encodeFile = open(encoded_file, 'r', encoding='utf-8-sig')
    except FileNotFoundError:
        raise IOError('Input File Not Found')
    for line in encodeFile:
        for char in line:  # each char is either 0 or 1
            # for each char i need to go to the tree respectively 0 goes to left and 1 goes to the right tree
            if char == '0':
                faketree = faketree.left
            elif char == '1':
                faketree = faketree.right
            else:
                raise IOError
            if faketree.left is None and faketree.right is None:
                text += chr(faketree.char)
                faketree = tree
    encodeFile.close()
    #print(text)
    endFile = open(decode_file, 'w')
    endFile.truncate()
    endFile.write(text)
    endFile.close()


# PART B
# takes a node and converts it to text? in an understandable sort of way
# add a 0 for nonleaf nodes add a 1 and its character for leaf nodes
# HuffmanNode -> String
def tree_preord(node):
    return tree_preord_write(node, '')


def tree_preord_write(node, str):
    if node is not None:
        if node.left is None and node.right is None:
            str += '1' + chr(node.char)
            return str
        str = tree_preord_write(node.left, str+'0')
        str = tree_preord_write(node.right, str)
    return str
