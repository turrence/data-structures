''' 
Name: Terence Tong
Section: 202 - 9
'''

class StackArray:
	"""Implements an efficient last-in first-out Abstract Data Type using a Python List"""
        
	def __init__(self, capacity):
		"""Creates and empty stack with a capacity"""
		self.capacity = capacity		# this is example for list implementation
		self.items = [None]*capacity 		# this is example for list implementation
		self.num_items = 0 			# this is example for list implementation

	def is_empty(self):
		"""Returns true if the stack self is empty and false otherwise"""
		if self.num_items == 0:
			return True
		return False
		
	def is_full(self):
		"""Returns true if the stack self is full and false otherwise"""
		if self.num_items == self.capacity:
			return True
		return False

	def push(self, item):
		if(self.is_full()):
			raise IndexError
		else:
			self.items[self.num_items] = item
			self.num_items += 1
			
			
	def pop(self):
		if (self.is_empty()):
			raise IndexError("there is nothing left to pop")
		else:
			self.num_items -= 1
			temp = self.items[self.num_items]
			self.items[self.num_items] = None
			return temp
			
		
	def peek(self):
		if self.is_empty():
			return None
		else:
			return self.items[self.num_items-1]
	def size(self):
		"""Returns the number of elements currently in the stack, not the capacity"""
		return self.num_items
		
	def __repr__(self):
		return ('StackArray({}), Capacity: {}').format(self.items, self.capacity)
	
	def __eq__(self, other):
		return self.items == other.items

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
	def getNext(self):
		return self.next
	
	def getData(self):
		return self.data
		
	def setNext(self, next):	
		self.next = next
		
	def setData(self, data):
		self.data = data
	
	def __repr__(self):
		return self.getData()
	'''
	def __eq__(self,other):
		if other == None:
			return False
		return self.data == other.data
	'''

class StackLinked:
	"""Implements an efficient last-in first-out Abstract Data Type using a Python List"""
        
	def __init__(self, capacity):
		"""Creates and empty stack with a capacity"""
		self.capacity = capacity		# this is example for list implementation
		self.items = None# this is example for list implementation
		self.num_items = 0 			# this is example for list implementation

	def is_empty(self):
		"""Returns true if the stack self is empty and false otherwise"""
		if self.num_items == 0:
			return True
		return False
		
	def is_full(self):
		"""Returns true if the stack self is full and false otherwise"""
		if self.num_items == self.capacity:
			return True
		return False	

	def push(self, item):
		numOfItem = 1
		node = Node(item)
		if self.is_full():
			raise IndexError
		'''
		if not lastItem.getNext() == None: #check if the node has other nodes attached to it
			while(not lastItem.getNext() == None): #runs a loop to see how many nodes are connected
				numOfItem += 1 #adds numOfItem for each additional node attatched
				lastItem = lastItem.getNext() #changes the conditional of the while loop to keep looping
			if numOfItem + self.num_items > self.capacity: # checks to see the chain of nodes is not larger than the capacity
				raise IndexError
		'''
		self.num_items += 1 #numOfItem
		if self.items == None: #so we dont have the initial empty node initially
			self.items = node
		else: 
			temp = self.items
			self.items = node
			node.setNext(temp) # accounts for mutiple nodes added

	def pop(self):
		if self.is_empty():
			raise IndexError	
		else:
			self.num_items -= 1
			temp = self.items
			self.items = self.items.getNext()
			return temp.getData()

	def peek(self):
		return self.items.getData()
		
	def size(self):
		"""Returns the number of elements currently in the stack, not the capacity"""
		return self.num_items
		
	def __repr__(self):
		return ('StackLinked(Nodes: {}, Capacity: {}), ').format(self.items, self.capacity)
		
	def __eq__(self, other):
		return self.items == other.items and self.capacity == other.capacity and self.num_items == other.num_items
'''
stacklink = StackLinked(5)
stacklink1 = StackLinked(5)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
stacklink.push(node1)
stacklink.push(node2)
print(node3.getNext())
stacklink.push(node3)
stacklink.push(node4)
stacklink.push(node5)
stacklink1.push(node1)
stacklink1.push(node2)
stacklink1.push(node3)

print(stacklink == stacklink1)
print(stacklink1.capacity)
'''