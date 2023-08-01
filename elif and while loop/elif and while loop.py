correctnumber = 5
guess = 0 
while guess != correctnumber:
    guess = int(input("Guess the number: "))
    if guess != correctnumber:
        print("False guess")
print("You guessed the correct number")

correctnumber = 5
guess = 0
while guess != correctnumber:
    guess = int(input("Guess the number: "))
    if guess != correctnumber:
        print('False guess')

numBuildings = 2
aptsperBuilding = 3
aptnum = 1

while aptnum <= aptsperBuilding:
    month = 1
    while month <= 12:
        building = 1
        while building <= numBuildings:
            print("-Payment Coupon-------")
            print("Building", building)
            print("aptnum", aptnum)
            print("Month:", month)
            print("Rent Due:800 ")
            print("----------------")
            building = building + 1
        month = month + 1
    aptnum = aptnum + 1 

print('You guess the correct number')

c = 1
while c < 5:
    print(c, "This is inside of while loop")
    c+=1
else:
    print(c, "This is outside of while loop")

word = "Anaconda"
pos = 0
while pos < len(word):
    print(word[pos])
    pos+=1


print("Printing multiples of 3 from 1 to 10")
i = 1
while i < 11:
    print(3*i)
    i = i + 1
print("Rest of the program")

i = 1
while i < 11:
    j = 0
    while j < i:
        print('*', end=" ")
        j = j + 1
    print()
    i = i + 1
print("Rest of the program")


for name in ('Rafey','Rashid','Naeem','Kashif','Shahzeb'):
    print(name, end=" CS Studenet")
    print()

i = 1
j = 5
while i < 4:
    while j < 8:
        print(i, ",", j)
        j = j + 1
        i = i + 1

num = eval(input("Enter the number to check: "))
if 9 < num < 99:
    print("Two digits number")
elif 99 < num < 999:
    print("Three digit number")
elif 999 < num < 9999:
    print("Four digit number") 
else:
    print("number is <= 9 or >= 9999")

    i = 0
while i < 5:
    j = 0
    while j < 5:
        if j <= i:
            print(j+1, end="")
        j +=1
    print("")
    i +=1