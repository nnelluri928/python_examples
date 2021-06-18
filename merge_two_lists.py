def merge_gen(a,b):
    for item1,item2 in zip(a,b):
        yield item1
        yield item2


a = ["a","b","c","d"]
b = [1,2,3,4]
print(list(merge_gen(a,b)))


#second solution

from itertools import chain
print(list(chain.from_iterable(zip(a,b))))