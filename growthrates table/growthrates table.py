def growthrates (n):
    'print values of below 3 function for i = 1, ..., n '
    print(' i      i**2     i**3    2**i')
    formatStr = '{0:2d}  {1:6d}  {2:6d}  {3:6d}'
    for i in range (2, n+1):
        print(formatStr.format(i, i**2, i**3, 2**i))
print(growthrates(20))


print("i    i**2     i**3      2**i")
for i in range (1,13):
    print(f"{i}      {i**2}       {i**3}       {2**i}")



table = str.maketrans('abcdef','uvwxyz')
print(table)
print(chr(97),chr(117))
print('fad'.translate(table))
print('desktop'.translate(table))