# Name: Terence Tong
# Class: CSC 202 - 9

class MyHashTable:
    def __init__(self, table_size=11):
        self.hash_table = [[] for _ in range(table_size)]
        self.num_items = 0

    # this function takes a key, and an item. Keys are valid Python non-negative integers. The function will insert
    # the key-item pair into the hash table based on the hash value of the key mod the table size
    # (hash_value = key % table_size). If the key-item pair being inserted into the hash table is a duplicate key,
    # the old key-item pair will be replaced by the new key-item pair. If the insert would cause the load factor of
    # the hash table to become greater than 1.5, the number of slots in the hash table should be increased to twice
    # the old number of slots, plus 1 (new_size = 2*old_size + 1). After creating the new hash table, the items in the
    # old hash table need to be rehashed into the new table.
    # int, item -> None
    def insert(self, key, item):
        hashValue = key % len(self.hash_table)
        if not self.hash_table[hashValue]:  # checks if its empty
            self.hash_table[hashValue].append((key, item))
            self.num_items += 1
        else:
            exists = False
            for i in range(len(self.hash_table[hashValue])):
                if self.hash_table[hashValue][i][0] == key:
                    lst = list(self.hash_table[hashValue][i])
                    lst[1] = item
                    self.hash_table[hashValue][i] = tuple(lst)
                    # self.num_items should stay the same
                    exists = True
                    break
            if not exists:
                self.hash_table[hashValue].append((key, item))
                self.num_items += 1
        if self.load_factor() > 1.5:
            newSize = 2 * len(self.hash_table) + 1
            tableCopy = self.hash_table
            self.hash_table = [[] for _ in range(newSize)]
            self.num_items = 0
            for hashIndex in tableCopy:
                for tup in hashIndex:
                    self.insert(tup[0], tup[1])

    # this function takes a key and returns the item (key, item) pair from the hash table associated with the key.
    # If no key-item pair is associated with the key, the function raises a LookupError exception.
    # int -> (key, item) tuple btw
    def get(self, key):
        hashValue = key % len(self.hash_table)
        for tup in self.hash_table[hashValue]:
            if tup[0] == key:
                return tup
        raise LookupError

    # this function takes a key, removes the key-item pair from the hash table and returns the key-item pair.
    # If no key-item pair is associated with the key, the function raises a LookupError exception.
    # int -> tuple (key, item)
    def remove(self, key):
        hashValue = key % len(self.hash_table)
        for i in range(len(self.hash_table[hashValue])):
            if self.hash_table[hashValue][i][0] == key:
                self.num_items -= 1
                return self.hash_table[hashValue].pop(i)
        raise LookupError

    # this function returns the number of key-item pairs currently stored in the hash table.
    # None -> int
    def size(self):
        return self.num_items

    # this function returns the current load factor of the hash table.
    # None -> float
    def load_factor(self):
        return self.size() / len(self.hash_table)

    # this function returns the number of collisions that have occurred during insertions into the hash table.
    # A collision occurs when an item is inserted into the hash table at a location where one or more key-item pairs
    # has already been inserted. When the table is resized, do not increment the number of collisions unless a
    # collision occurs when the new key-item pair is being inserted into the resized hash table.
    def collisions(self):
        counter = 0
        for hasharr in self.hash_table:
            col = 0
            for i in range(len(hasharr)):
                if i != 0:
                    col += 1
            counter += col
        return counter

    def __repr__(self):
        return 'HashTable({})'.format(self.hash_table)