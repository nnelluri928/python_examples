'''
As we return the unsigned int, the bytes are left shifted so that they are properly aligned and then a logical OR 
is applied to combine the bytes. The result of this is a 32-bit representation of the IP address. 
In this case, the resulting integer in decimal is 3,232,235,521. 
The table below shows what the left shift looks like in memory.

Variable	Byte 0	Byte 1	Byte 2	Byte 3	Operation
Byte[3]				00000001	N/A
Variable	Byte 0	Byte 1	Byte 2	Byte 3	Operation
Byte[2]				00000000	
8
Result			00000000	00000000	
Variable	Byte 0	Byte 1	Byte 2	Byte 3	Operation
Byte[1]				10101000	
16
Result		10101000	00000000	00000000	
Variable	Byte 0	Byte 1	Byte 2	Byte 3	Operation
Byte[0]				11000000	
24
Result	11000000	00000000	00000000	00000000	
And the OR operation:
Variable	Byte 0	Byte 1	Byte 2	Byte 3	Operation
Byte[0]	11000000	00000000	00000000	00000000	
Byte[1]		10101000	00000000	00000000	OR
Result	11000000	10101000	00000000	00000000	
Byte[2]			00000000	00000000	OR
Result	11000000	10101000	00000000	00000000	
Byte[3]				00000001	OR
Result	11000000	10101000	00000000	00000001	



'''


def dotted_decimal_to_int(s):
    oct1,oct2,oct3,oct4 = s.split(".")
    return int(oct1) << 24 | int(oct2) << 16 | int(oct3) << 8 | int(oct4)

print(dotted_decimal_to_int('192.168.0.1'))