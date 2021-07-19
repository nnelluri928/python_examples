val = 3232235521

def dotted_decimal_to_int(val):
        return '.'.join([str(val >> (i << 3) & 0xFF)   
                for i in range(4)[::-1]])

print(dotted_decimal_to_int(val))