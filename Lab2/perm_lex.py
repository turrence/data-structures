#Name: Terence Tong
#Section: 202 - 9

# Data Types: string to permutate all combinations
# input -> output: string to be permuted -> list of all possible combinations of the string

def perm_gen_lex(word):
	if word == "":
		return []
		
	if len(word) <= 1: #If the string contains a single character return a list containing that string
		return [word]
		
	resultList = []
	for i in range(len(word)): #Loop through all character positions of the string containing the characters to be permuted
		smallerStr = word.replace(word[i], '') # Form a simpler string by removing the character
		permutations = perm_gen_lex(smallerStr) # Generate all permutations of the simpler string recursively
		for perm in permutations: 	#Add the removed character to the front of each permutation of the simpler word
			resultList.append(word[i] + perm) #add the resulting permutation to a list
	return resultList # return all newly constructed permutations
