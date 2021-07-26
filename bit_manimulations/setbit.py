

def set_bit(x,position):
    mask = 1 << position
    return x | mask

print(set_bit(0b00000101,0b00000101))

def clear_bit(x,position):
    mask = 1 << position
    return x & ~mask
print(clear_bit(0b00000101,0b00000010))

def flip_bit(x,position):
    mask = 1 << position
    return x ^ mask

print(flip_bit(5,2))

def is_bit_set(x,position):
    shifted = x >> position
    return bool(shifted & 1)

print(is_bit_set(101,5))

def count_bits(x):
    mask = 128
    count =0
    for i in range(9):
        if x & mask !=0:
            count +=1
        mask >>=1
    return count 
print(count_bits(255))

def modify_bit(x,position,state):
    mask = 1 << position
    return (x & ~mask) | (-state & mask)

print(modify_bit(6,3,0))

'''
check if number is even
(x & 1) == 0

check if number is power of two
(x & x-1) == 0
EX:
write a function to count the numbe of bits
that are differnt between two numbers
'''