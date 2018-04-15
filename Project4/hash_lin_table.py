# Terence Tong
# CSC 202 - 9

# num_stops and stop_table need to be taken out
class HashTableLinPr:
    def __init__(self, size=251):
        self.hash_table = [()] * size
        self.num_items = 0

    # read words from a stop words file and insert them into hash table
    # file -> None
    def read_stop(self, filename):
        file = open(filename, encoding='utf-8-sig')
        self.hash_table = ['']*251
        for word in file:  # works because word per line file
            self.insert_stop_table(word)
            if self.get_load_fact() > 0.75:
                #print('rehashing...')
                newSize = len(self.hash_table) * 2 + 1
                copyTable = self.hash_table
                self.hash_table = ['']*newSize
                self.num_items = 0
                for copy in copyTable:
                    if copy == '':
                        continue
                    else:
                        self.insert_stop_table(copy)
        file.close()

    # inserts a word from stop_words.txt assume text by line
    # string, array -> None
    def insert_stop_table(self, word):
        actualWord = word.strip('\\\n')  # deletes the \n in the word
        hashValue = self.myhash(actualWord, len(self.hash_table))
        while self.hash_table[hashValue] != '':  # assumes no repeats
            hashValue += 1
            if hashValue == len(self.hash_table):
                hashValue = 0
        self.hash_table[hashValue] = actualWord
        self.num_items += 1

    # read words from input file and insert them into hash table,
    # after processing for punctuation, numbers and filtering out stop words in the stop_table
    # filename, HashTableLinPr -> None
    def read_file(self, filename, stop_table):
        file = open(filename)
        lineNum = 1
        for line in file:
            arr = line.split()
            insert_words = []
            # self.filter_string(arr)
            #print('all words', arr)
            # because stop_table has apostrophe's remove_punctuation deletes everything except apostrophe
            for word in arr:
                if self.is_number(self.remove_punctuation(word)) or self.remove_punctuation(word.lower()) \
                        in stop_table.hash_table:
                    continue
                else:
                    insert_words.append(self.remove_punctuation(word.lower()))  # words with punctuation at the end
            #print('to be inserted words: ', insert_words)
            self.filter_string(insert_words)
            #print('modified inserted words', insert_words)
            for word in insert_words:
                if not word in stop_table.hash_table:
                    self.insert_word(word, lineNum)
            if self.get_load_fact() > .75:
                self.rehash()
            lineNum += 1

    # removes all punctuation from the word except apostrophes
    # string -> string
    def remove_punctuation(self, word):
        char_index = 0
        new = word
        while char_index < len(new):
            if new[char_index] in '?!.,():;\"':
                new = new.replace(new[char_index], '')
                char_index -= 1
            char_index += 1
        return new

    # inserts a word into self.hash_table
    # words are the same just change the line number
    # string, int -> None
    def insert_word(self, word, line_num):
        hashValue = self.myhash(word, len(self.hash_table))
        while self.hash_table[hashValue] and self.hash_table[hashValue][0] != word:
            #print('collision at', hashValue, "with", self.hash_table[hashValue], 'for', word)
            hashValue += 1  # linear probing
            if hashValue >= len(self.hash_table):
                hashValue = 0
        if not self.hash_table[hashValue] and type(line_num) is not list:
            self.hash_table[hashValue] = (word, [line_num])
            self.num_items += 1
        elif not self.hash_table[hashValue] and type(line_num) is list:
            self.hash_table[hashValue] = (word, line_num)
            self.num_items += 1
        elif self.word_exists_in_line(hashValue, line_num):
            return
        elif self.hash_table[hashValue][0] == word:
            self.hash_table[hashValue][1].append(line_num)
        if self.get_load_fact() > 0.75:
            self.rehash()

    # checks if the line_num exists in the word's array
    # int, int -> boolean
    def word_exists_in_line(self, hashValue, line_num):
        for num in self.hash_table[hashValue][1]:
            if num == line_num:
                return True
        return False

    # rehash the self.hash_table and increases the size of the self.hash_table
    # None -> None
    def rehash(self):
        #print('rehashing...')
        copyTable = self.hash_table
        newSize = len(self.hash_table)*2 + 1
        self.hash_table = [()]*newSize
        self.num_items = 0
        for copyDict in copyTable:
            if copyDict == ():
                continue
            else:
                self.insert_word(copyDict[0], copyDict[1])

    # changes the arr_string taking out punctuation and lowercases the word
    # final filter, removes everything including apostrophes to write to list
    def filter_string(self, arr_string):
        index = 0
        while index < len(arr_string):  # removes punctuation and lowercases the word
            arr_string[index] = arr_string[index].lower()
            arr_string[index] = arr_string[index].strip('\\\n')
            i = 0
            while i < len(arr_string[index]):
                if arr_string[index][i] in "?!.,():;\"\' ":
                    arr_string[index] = arr_string[index].replace(arr_string[index][i], '')
                elif arr_string[index][i] == "-":
                    arr_string.append(arr_string[index][i+1:])
                    arr_string[index] = arr_string[index][:i]
                    break
                i += 1
            index += 1

    # returns the size of the hash table
    # None -> int
    def get_tablesize(self):
        return self.num_items

    # writes out the concordance to output_filename based on self.hash_table
    # output_filename -> None
    def save_concordance(self, output_filename):
        file = open(output_filename, 'w')
        file.truncate()
        listPair = []
        wordList = []
        for thing in self.hash_table:
            if thing != ():
                listPair.append(thing)
        for wordLine in listPair:
            wordList.append(wordLine[0])
        wordList = sorted(wordList)
        for i in range(len(listPair)):
            temp = sorted(listPair[i][1])
            listPair[i] = (listPair[i][0], temp)
        i = 0
        j = 0
        while i < len(listPair):
            j = 0
            while j < len(listPair):
                if wordList[i] == listPair[j][0]:
                    wordList[i] = listPair[j]
                    break
                j += 1
            i += 1
        stri = ""
        for i in range(len(wordList)):
            stri += wordList[i][0]
            stri += ':\t'
            nums = ""
            for digit in wordList[i][1]:
                nums += str(digit)
                nums += " "
            stri += nums[:-1]
            if i != len(wordList) - 1:
                stri += '\n'
        file.write(stri)
        file.close()

    # returns the load factor of the table
    # None -> float
    def get_load_fact(self):
        return self.get_tablesize() / len(self.hash_table)

    # checks if s is a number
    # item -> boolean
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    # return an integer from 0 to the (size of the hash table)  1.
    # Compute the hash value by h_value(str) = Σ𝑛−1 𝑜𝑟𝑑(𝑠𝑡𝑟[𝑖]) ∗ 31^𝑛−1−𝑖
    # where n = the minimum of len(key) and 8 (e.g., if len (key) > 8 assume n=8) , i = the index of each
    # character of the key.
    # string, int -> int
    def myhash(self, key, table_size):
        length = len(key)
        # convert key to everything lowercase or uppercase up to me
        hashValue = 0
        i = 0
        for char in key:
            hashValue += ord(char) * 31 ** length-1-i
            i += 1
        # print(hashValue % table_size)
        return hashValue % table_size

    def __repr__(self):
        return 'HashTableLinePr({})'.format(self.hash_table)