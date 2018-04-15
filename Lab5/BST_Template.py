# final version for class notes

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, newkey):
        
        if self.root is None:			 # if tree is empty
            self.root = TreeNode(newkey)
            return
        else:
            p = self.root
            if p.key > newkey:
                if p.left is None:
                    p.left = TreeNode(newkey)
                else:
                    p.left.insert(newkey)
            else:
                if p.right is None:
                    p.right = TreeNode(newkey)
                else:
                    p.right.insert(newkey)

    def find (self, key):
        p = self.root      # current node
        while p is not None and p.key != key :
            if key < p.key:
                p = p.left
            else:
                p = p.right

        if p is None :
            return False	    
        else:
            return True     # might want to return the node or ???


   
    
class TreeNode:
    """Tree node: left and right child + data which can be any object"""

    def __init__(self,key):

        self.key = key  
        self.data = None

    def insert(self, key):
        """  Insert new node with key, assumes data not present """
        if self.key != None:
            if key < self.key:
                if self.left is None:
                    self.left = TreeNode(key)
                else:
                   self.left.insert(key)
            elif key > self.key:
                if self.right is None:
                    self.right = TreeNode(key)
                else:
                    self.right.insert(key)
        else:
            self.key = key

    def print_tree(self):

        """   Print tree content inorder        """

        if (self.left != None):
            self.left.print_tree()
            
        print(self.key, end=", ")
        
        if (self.right != None):
            self.right.print_tree()


t = BinarySearchTree()
t.insert(3)
t.insert(10)
t.insert(1)
print ("\nTree after inserting 8, 3, 10, 1")
t.root.print_tree()
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(14)
t.insert(13)
print ("\nTree after inserting 6, 4, 7, 14, 13")
t.root.print_tree()

print("\nTesting find 14")
print(t.find(14))
print("Testing find 15")
print(t.find(15))
