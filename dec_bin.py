num = -19

if num < 0:
    isNeg = True
    num =abs(num)
else:
    isNeg = False

res =''
while num > 0:
    res = str(num%2) + res
    num = num //2
if isNeg:
    res = '-' + res
print(res)