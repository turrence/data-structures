"""
Name: Terence Tong
Section: CSC 202 - 9
"""


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key  # primitive data types
        self.data = None  # object types that contain the primitive data types
        self.parent = None

    # None -> None
    # inserts a TreeNode in the appropriate location to maintain a binary tree
    def insert(self, key):  # inserts a node with key into the correct position if not a duplicate.
        if self.key is not None:
            if key < self.key:
                if self.left is None:
                    self.left = TreeNode(key)
                    self.left.parent = self
                else:
                    self.left.insert(key)
            elif key > self.key:
                if self.right is None:
                    self.right = TreeNode(key)
                    self.right.parent = self
                else:
                    self.right.insert(key)
        else:
            self.key = key

    # None -> return TreeNode successor
    # finds a successor of the TreeNode for the case you gotta delete a TreeNode
    def find_successor(self):  # returns the node that is the inorder successor of the node
        succ = None
        if self.right is not None:  # find the min of the right tree which is supposed to be the successor
            succ = self.right.find_min_node()
        else:  # self.right is None or there is a left child
            if self.parent:  # the parent exists aka not the root
                if self.parent.left is self:  # there is a left to child to this node and there is no right one
                    succ = self.parent
                else:  # self.parent.right is self
                    self.parent.right = None
                    succ = self.parent.findSuccessor()  # the successor is the parent's successor excluding this node
                    self.parent.right = self
        return succ

    # None -> min value in tree
    def find_min(self):  # returns min value in the tree
        if self.left is None:
            return self.key
        left = self.left
        while left.left is not None:
            left = left.left
        return left.key

    # None -> min node in tree
    def find_min_node(self):
        if self.left is None:
            return self.key
        left = self.left
        while left.left is not None:
            left = left.left
        return left

    # None -> max value in tree
    def find_max(self):  # returns max value in the tree
        if self.right is None:
            return self.key
        right = self.right
        while right.right is not None:
            right = right.right
        return right.key

    # prints the tree in order (left, root, right)
    def inorder_print_tree(self):  # print inorder the subtree of self left tree, root, right tree
        if self.left is not None:
            self.left.inorder_print_tree()

        print(self.key, end="   ")

        if self.right is not None:
            self.right.inorder_print_tree()

    # inorder traversal prints list of pairs, [key, level of the node] where root is level 0
    def print_levels(self):
        if self.left is not None:
            self.left.print_levels()

        print(self.key, self.countLevel(), end="   ")

        if self.right is not None:
            self.right.print_levels()

    # helper function for print_levels which counts the level of the node
    def countLevel(self):
        temp = self.parent
        count = 0
        while temp is not None:
            temp = temp.parent
            count += 1
        return count

    def hasAnyChildren(self):
        return self.left or self.right

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    # deletes self TreeNode doesnt quite preserve order
    def spliceOut(self):
        if self.isLeaf():
            if self.isRightChild():
                self.parent.right = None
            else:
                self.parent.left = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:  # self.hasRightChild
                if self.isRightChild():
                    self.parent.right = self.right
                else:
                    self.parent.right = self.left
                self.right.parent = self.parent


class BinarySearchTree:
    # im pretty sure root is a tree node
    def __init__(self):
        self.root = None

    def find(self, key):  # returns True if key is in a node of the tree, else False
        if self.root is None:
            return False
        temp = self.root
        while temp is not None and temp.key != key:
            if key > temp.key:
                temp = temp.right
            elif key < temp.key:
                temp = temp.left
        if temp is None:
            return False
        if key == temp.key:
            return temp

    def insert(self, newkey):
        if self.root is None:
            self.root = TreeNode(newkey)
        else:
            self.root.insert(newkey)

    # deletes the node containing key, assumes such a node exists and modifies the tree so its still BST
    # int -> None
    def delete(self, key):
        node = self.find(key)  # assumes it exists based on given parameters
        if node.isLeaf():  # handles if node has no children ezPz
            if node.isLeftChild():
                node.parent.left = None
            else:
                node.parent.right = None
        # the following if statements in the blocks of may seem scary, but they just handle which parent data field to
        # change and which node children field to change except for the last condition which is really smart
        elif node.hasLeftChild() and not node.hasRightChild():
            if node.isLeftChild():  # node both is and has a left child
                node.left.parent = node.parent
                node.parent.left = node.left
            elif node.isRightChild():  # node has left child and is right child
                node.left.parent = node.parent
                node.parent.right = node.left
            else:  # is a root
                node.left.parent = None
                self.root = node.left
        elif node.hasRightChild() and not node.hasLeftChild():  # node has right child
            if node.isLeftChild():  # node is a left child and has a right child
                node.right.parent = node.parent
                node.parent.left = node.right
            elif node.isRightChild():  # node is a right child and has a right child
                node.right.parent = node.parent
                node.parent.right = node.right
            else:
                node.right.parent = None
                self.root = node.right
        else:  # has both a left child and a right child
            succ = node.find_successor()  # finds the appropriate successor
            succ.spliceOut()  # deletes where the successor node was
            node.key = succ.key  # changes the node key to preserve order
            node.data = succ.data  # changes the node data to preserve order
            # delete in this case deletes the successor from its place and in turn changes the node intentionally to be
            # deleted data and key values instead of actually replacing it with an entirely different node

    # print inorder the entire tree
    def print_tree(self):
        self.root.inorder_print_tree()

    # None -> boolean
    def is_empty(self):  # returns True if tree is empty, else False
        return self.root is None
