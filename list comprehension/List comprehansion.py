l = [ i for i in range(6) if i%2==0]
for i in range(5):
     if i % 2 == 0:
          
        l.append(i)

print(l)

l = []
for i in range(6):
    if i % 2 == 0:
        l.append(i)
print(l)
l = [i for i in range(6) if i % 2 == 0]
print(l)
l = [i for i in range(7) if i % 2 == 0]
print(l)
l = []
for i in range(7):
    if i % 2 == 0:
        l.append(i)
print(l)
l = [i for i in range(9) if i % 2 == 0 ]
print(l)
l = []
for i in range(9):
    if i % 2 == 0:
        l.append(i)
print(l)
l = [i for i in range(8) if i % 3 == 0]
print(l)
l = []
for i in range(8):
    if i % 3 == 0:
        l.append(i)
print(l)
l = [i for i in range(8) if i % 3 == 0]
print(l)
l = [[0 for col in range(3)] for row in range(3)]
print(l)
[[0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0]]
for row in range(3):
    for col in range(3):
        l[row][col] = row * col
print(l)


datalist = [300, 12.65, 5+6j, True, 'Faisal', (5, -7), [8, 52],{"color":'blue', "color":'red'}]
for i in datalist:
    print(type(i), end=" ")