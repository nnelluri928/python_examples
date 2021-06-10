'''
Assume we are working with a dictionary whose values are all unique numbers. 
Write a function that returns the key that maps to the largest value in the dictionary.
'''
def max_key(x):
    max_val = max(x.values())
    for k,v in x.items():
        if v == max_val:
            return k


print(max_key({'a': 0, 'b': 2, 'c': 200, 'd': 0}))


'''
Here, we pass it the built-in dictionary-function get, 
which takes in a dictionary’s key as an argument, and returns the 
corresponding value from the mapping. Thus max will iterate over each key of x, 
and discern the maximum value by comparing the value returned by each x.get(key) 
(which is effectively the same as x[key]).
'''

def max_key_optimal(x):
    return max(x,key=x.get)


print(max_key_optimal({'a': -1, 'b': 30, 'c': 10, 'd': 500}))

