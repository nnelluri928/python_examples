'''
>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]

>>> matrix1 = [[1, 9], [7, 3]]
>>> matrix2 = [[5, -4], [3, 3]]
>>> matrix3 = [[2, 3], [-3, 1]]
>>> add(matrix1, matrix2, matrix3)
[[8, 8], [7, 7]]
>>> add([[1, 9], [7, 3]], [[1, 2], [3]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "add.py", line 10, in add
    raise ValueError("Given matrices are not the same size.")
ValueError: Given matrices are not the same size.

'''


def add(matrix1,matrix2):
    combined =[]
    for row1,row2 in zip(matrix1,matrix2):
        row = [
            n+m
            for n,m in zip(row1,row2)
            ]
        combined.append(row)
    return combined


matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
print(add(matrix1, matrix2))

def add(matrix1,matrix2):
    combined = []
    for row1,row2 in zip(matrix1,matrix2):
        combined.append([n+m for n,m in zip(row1,row2)])
    return combined
matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
print(add(matrix1, matrix2))

#We can copy-paste this loop into another comprehension:
def add(matrix1,matrix2):

    return [
        [n+m for n,m in zip(row1,row2)]
        for row1,row2 in zip(matrix1,matrix2)
    ]
matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
print(add(matrix1, matrix2))

'''
Bonus #1
For the first bonus we need to accept any number of matrices.
To do this we'll need to accept any number of arguments to our function 
and pass any number of arguments to the zip function. 
We can use the * operator for this.
'''

def add(*matrices):
    combined = []
    for rows in zip(*matrices):
        row = []
        for values in zip(*rows):
            row.append(sum(values))
        combined.append(row)
    return combined

matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
matrix3 = [[2, 3], [-3, 1]]
print(add(matrix1,matrix2,matrix3))


def add(*matrices):
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]
matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
matrix3 = [[2, 3], [-3, 1]]
print(add(matrix1,matrix2,matrix3))

'''
Bonus #2
For the second bonus, we were supposed to raise a ValueError exception 
when our lists-of-lists were different shapes.

This might seem a little complex. We're using a set here because set items are unique 
so if we pass in objects that are equal, 
we should only end up with 1 item in our set.
We can't pass in a list because lists aren't "hashable" 
because they're mutable (they can be changed). 
Tuples can be hashable so we're passing a generator expression into the tuple constructor 
inside a set comprehension to make a set of tuples.
'''
def add(*matrices):
    matrix_shapes = {
    tuple(len(r) for r in matrix)
    for matrix in matrices
    }
    if len(matrix_shapes) > 1:
        raise ValueError("Given matrices are not the same size.")
    return [
    [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]

#print(add([[1, 9], [7, 3]], [[1, 2], [3]]))
#Here's another answer:
'''
Python's built-in zip function stops at the shortest list when zipping.

The zip_longest function in the itertools module uses a fill value to return missing items 
so the resulting list is as long as the longest gives list.
The default fill value for zip_longest is None, so looping over None would fail and 
adding None to a number would fail too. In both cases we'd get a TypeError 
which is why we're catching a TypeError to handle the case where matrices aren't the same size.
That raise X from Y syntax we're using is a Python 3 feature to make tracebacks more clear.
'''
from itertools import zip_longest
def add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    try:
        return [
            [sum(values) for values in zip_longest(*rows)]
            for rows in zip_longest(*matrices)
        ]
    except TypeError as e:
        raise ValueError("Given matrices are not the same size.") from e
print(add([[1, 9], [7, 3]], [[1, 2], [3]]))