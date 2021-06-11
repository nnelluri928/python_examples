'''
Merge two dictionaries together such that the resulting dictionary always 
retain the greater value among mappings with common keys.
'''
def opt_merge_max_mappings(dict1, dict2):
    """ Merges two dictionaries based on the largest value in a given mapping.
    """
    # we will iterate over `other` to populate `merged`
    merged,other =(dict1,dcit2) if len(dict1) > len(dict2) else (dict2, dict1)
    merged = dict(merged)
    for key in other:
        if key not in merged or other[key] > merged[key]:
            merged[key] = other[key]
    return merged
dict1 = {'bananas': 7, 'apples': 3, 'pears': 14}
dict2 = {'bananas': 3, 'apples': 6, 'grapes': 9}
print(opt_merge_max_mappings(dict1, dict2))

#Extended Problem: Merging Arbitrary Numbers of Dictionaries


def merge_max_mappings(*dicts):
    merged = {}
    for d in dicts:
        for k in d:
            if k not in merged or d[k] > merged[k]:
                merged[k] = d[k]
    return merged



a = dict(a=0, b=100, c=3)
b = dict(a=10, b=10)
c = dict(c=50)
d = dict(d=-70)
e = dict()
print(merge_max_mappings(a,b,c,d,e))