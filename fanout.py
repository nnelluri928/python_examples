'''
Given a list of numbers, for each number generate a list of the differences 
between it and ππππππ’π‘nfanout (known as the fanout value) following numbers in the list. 
Return a list of all the lists generated for each number. 
For members in the list that have fewer than ππππππ’π‘nfanout following members, 
calculate as many differences as possible. For example, suppose we want to compute the 
difference fanout on the list [3, 2, 4, 6, 1] with a fanout value of 3. 
Then we would compute:
β’	3β[2β3,4β3,6β3]3β[2β3,4β3,6β3]
β’	2β[4β2,6β2,1β2]2β[4β2,6β2,1β2]
β’	4β[6β4,1β4]4β[6β4,1β4]
β’	6β[1β6]6β[1β6]
β’	1β[]

'''
'''
Solution: difference_fanout using for-loops
We will naturally tackle this problem by performing nested for-loops. 
The outermost for-loop will loop over each number in the list. 
We will refer to this number as the βbase numberβ. 
We will want the inner for-loop to iterate ahead of the base number 
so that we can compute the differences between it and its ππππππ’π‘nfanout neighbors. 
We will need to take care re-initialize our intermediate list of differences 
for each new base number, otherwise each subtraction will get appended to one long list
'''
def difference_fanout(l, fanout):
    all_fanouts = []
    for i,base_number in enumerate(l):
        base_fanout = []
        for neighbor in l[i+1:i+1+fanout]:
            base_fanout.append(neighbor-base_number)
        all_fanouts.append(base_fanout)
    return all_fanouts

print(difference_fanout([3, 2, 4, 6, 1], 3))


'''
Solution: difference_fanout using list comprehensions
'''
def difference_fanout(l, fanout):

    return [[neighbor-base_number for neighbor in l[i+1:i+1+fanout]]
                for i,base_number in enumerate(l) ]
print(difference_fanout([3, 2, 4, 6, 1], 3))