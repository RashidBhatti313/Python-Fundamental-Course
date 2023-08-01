#                    DIAMOND PATTERN:

row = int(input("Enter the value of rows: "))
for i in range(row):
    print(" "*(row-i)+" *"*(i+1))

for j in range(row-1):
    print(" "*(j+2)+" *"*(row-1-j))

