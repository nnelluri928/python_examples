'''
An algorithm is required to test out what percentage of the parts that a factory is producing 
fall within a safety margin of the design specifications. Given a list of values recording 
the metrics of the manufactured parts, a list of values representing the desired metrics 
required by the design, and a margin of error allowed by the design, compute what 
fraction of the values are within the safety margin (<=)

# example behavior
>>> within_margin_percentage(desired=[10.0, 5.0, 8.0, 3.0, 2.0],
...                          actual= [10.3, 5.2, 8.4, 3.0, 1.2],
...                          margin=0.5)
0.8
'''
def within_margin_percentage(desired, actual, margin):
    count = 0  # tally of how values are within margin
    total = len(desired)
    for i in range(total):
        if abs(desired[i] - actual[i]) <= margin:
            count += 1  
    return count / total if total > 0 else 1.0




desired=[10.0, 5.0, 8.0, 3.0, 2.0]
actual= [10.3, 5.2, 8.4, 3.0, 1.2]
margin= 0.5

print(within_margin_percentage(desired,actual,margin))
print('-'*80)
print(within_margin_percentage([], [], margin=0.5))

'''
which is arguably the appropriate behavior for this scenario 
(no values fall outside of the margin). 
Had we not anticipated this edge case, within_margin_percentage([], [], margin=0.5) 
would raise ZeroDivisionError.

It is also possible to write this solution using the built-in 
sum function and a generator comprehension that filters out those pairs 
of items that fall outside of the desired margin:
'''

def opt_within_margin_percentage(desired, actual, margin):
    total = len(desired)
    count = sum(1 for i in range(total) if abs(actual[i] - desired[i]) <= margin)
    return  count / total if total > 0 else 1.0

print(opt_within_margin_percentage(desired,actual,margin))
print('-'*80)
print(opt_within_margin_percentage([], [], margin=0.5))
