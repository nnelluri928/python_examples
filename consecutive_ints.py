# Python program to check if the list contains consecutive integers
 
# Input : [2, 3, 1, 4, 5]
# Output : True
 
# Input : [1, 2, 3, 5, 6]
# Output : False
 
 
def checkConsecutive(l):
    return sorted(l) == list(range(min(l), max(l)+1))
 
lst = [2, 3, 1, 4, 5]
print(lst)
print(checkConsecutive(lst))
 
lst = [2, 3, 1, 4, 5, 7]
print(lst)
print(checkConsecutive(lst))
 
lst = [1, 2, 3, 5, 6]
print(lst)
print(checkConsecutive(lst))
 
lst = [33,35]
print(lst)
print(checkConsecutive(lst))
