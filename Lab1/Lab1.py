# Name: Terence Tong
# Section: CSC 202

# must use iteration not recursion
""" finds the max of a list of numbers and returns it, not the index"""
def max_list_iter(tlist):
	if(len(tlist) == 0):
		raise ValueError
	else:
		max = tlist[0]
		for num in tlist:
			if num > max:
				max = num
		return max
	
#must use recursion
" recursively reverses a list of numbers and returns it "
def reverse_rec(tempstr):
#	if len(tempstr) == 0:
#		return []
#	else:
#		return [tempstr.pop()] + reverse_rec(tempstr)
	if len(tempstr) == 0:
		return ""
	else:
		return tempstr[-1] + reverse_rec(tempstr[:-1])
		
# Binary Search
def bin_search(target, low, high, list_val):
	"""	Parameters
	@target- the number being searched for
	@low- the lower index to start the binary search with
	@high- the upper index to start the binary search with
	@list_val- the list being searched through
	"""
	list_val.sort()
	if len(list_val) == 0:
		return None
	mid = (low + high)//2 # midpoint between the indices
	if low <= high:
		if list_val[mid] == target: # base condition
			return mid
		elif target > list_val[mid]:
			return bin_search(target, mid+1, high, list_val) #runs another binary search the low index changed
		else:
			return bin_search(target, low, mid-1, list_val) #runs another search with the high index changed
	else:
		return None