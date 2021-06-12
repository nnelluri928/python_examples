'''
We want to encode a sequence of Python objects as a single string. 
The following describes the encoding method that we want to use for each type of object. 
Each object’s transcription in should be separated by " | ", and the result should be one large string.

If the object is an integer, convert it into a string by spelling out each digit in base-10 in this format: 
142 →
→one-four-two; -12 →
→neg-one-two.
If the object is a float, just append its integer part (obtained by rounding down) the same way and the string "and float": 12.324 →
→one-two and float.
If the object is a string, keep it as is.
If the object is of any other type, return '<OTHER>'.
# example behavior
>>> s = concat_to_str([12,-14.23,"hello", True,
...                    "Aha", 10.1, None, 5])
>>> s
'one-two | neg-one-four and float | hello | <OTHER> | Aha | one-zero and float | <OTHER> | five'
Tips: check out the isinstance function introduced here for handling different types. 
Also, consider creating a helper function for the conversion from integer to our special-format string, 
since we have to do it twice. It’s always good to extrapolate repeated tasks into functions. 
You’ll also need to hard-code the conversion from each digit to its English spell-out.
'''
'''
Solution

Our solution is broken down into three simple functions. 
int_to_str is used to map signed integers to English words. 
item_to_transcript is capable of mapping an object of any type to its string representation, 
in accordance with the prescription made by the problem statement. 
Finally, concat_to_str orchestrates these two helper functions, looping over each object in our input list, 
mapping each object to its string representation, and joining these strings with ' | '.
'''
def int_to_str(n):
    """
    Takes an integer and formats it into a special string
        e.g. 142 -> "one-four-two"
             -12 -> "neg-one-two"
    """
    mapping = {"0": "zero", "1": "one", "2": "two", "3": "three",
               "4": "four", "5": "five", "6": "six", "7": "seven",
               "8": "eight", "9": "nine", "-": "neg"}
    return "-".join(mapping[digit] for digit in str(n))

def item_to_transcript(item):
    if isinstance(item,bool): return '<OTHER>'
    if isinstance(item,int): return int_to_str(item)
    if isinstance(item,float):return int_to_str(int(item)) + ' and float'
    if isinstance(item,str): return item
    return '<OTHER>'

def concat_to_str(l):

    return " | ".join(item_to_transcript(item) for item in l)

s = concat_to_str([12,-14.23,"hello", True,"Aha", 10.1, None, 5])
print(s)