print("This program will count total number of vowelsfrom user defined sentences ")
string = input("Enter your string: ")
vowels = 0
for i in string:
    if (i == 'a'or i == 'e' or i == 'i' or i == 'o' or i == 'u'or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels=vowels+1
print("Number of vowels")
print(vowels) 

s = " Rashid Bhatti "
c = 0
for letter in s.lower():

    if letter == 'a' or letter =='i'  or letter == 'e' or letter == 'u' or letter=='o':
        c += 1
        print(letter, c)
print(c)