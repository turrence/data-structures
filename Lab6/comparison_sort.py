"""
Name: Rohan Ramani, Terence Tong
Section: 202 - 9
"""
import random

# creates and prints a random list of numbers
def listGenerator():
    alist = []
    for i in range(100000):
        # integer random numbers between 10 and 70
        n = random.randint(10, 70)
        alist.append(n)
    print(alist)
    return alist


'''
Terence Tong
write a insert sort algorithm
list of integers -> list of integers
'''
def insert_sort(alist):
    ind = 1
    comp = 0
    while ind < len(alist):
        j = ind
        while j > 0 and alist[j-1] > alist[j]:
            comp += 1
            temp = alist[j]
            alist[j] = alist[j-1]
            alist[j-1] = temp
            j -= 1
        ind += 1
    print('Insert Sort Comparisons:', comp)
    return alist

l1 = listGenerator()
l2 = l1.copy()
l2 = sorted(l2)
print(insert_sort(l1))
print(insert_sort(l2))
"""
Terence Tong
write an selection algorithm
list of integers -> list of integers
selection sort finds the smallest number and puts it in the front
"""
def select_sort(alist):
    comparisons = 0
    for i in range(len(alist)):
        minimum = alist[i]
        index = i
        for j in range(i, len(alist)):
            comparisons += 1
            if alist[j] < minimum:
                minimum = alist[j]
                index = j
        alist[index] = alist[i]
        alist[i] = minimum
    print('Select Sort Comparisons: ', comparisons)
    return alist

#print(select_sort(l1))
#print(select_sort(l2))

"""
Rohan Ramani
write a merge sort algorithm
list of integers -> list of integers
"""
def merge_sort(alist):
    pass
