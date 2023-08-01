s = "hello"
print(s[0:2])
print(s[3:4])
print(s[-3:-1])
print(s[-3:])

message = "This mesage is top secret and should not "
print(message.find('top secret'))
print(message.count('top secret'))
print(message.replace('top', 'no'))

public = message.replace('top', 'no')
print(public)

message = 'top secret'
print(message.capitalize())
print(message.upper())
print("za ghf fgf fdgfg dfgrdt".split(" "))
print("this is the text".split(" "))

x = '2;3;5;7;9;11;13'
print(x.split(";"))

table = str.maketrans('abcdef','uvwxyz')
print(table)
print(chr(97),chr(117))
print('fad'.translate(table))
print('desktop'.translate(table))

n = 5
print(n)

r = 5/3
print(n,r)
name = 'Ida'
print(n,r,name)
print(n,r,name,sep=";")
print(n,r,name,sep='\n')


for name in ['jeo','Sam','Tim','Ann']:
    print(name)
  

weekday = 'Wednesday'
month = 'March'
day = 10
year = 2010
hour = 11
minute = 45
second = 33    
print(weekday+', '+month+' '+str(day)+', '+str(year)+ ' at '+str(hour)+':'+str(minute)+':'+str(second))

print("i    i**2     i**3      2**i")
for i in range (1,13):
    print(f"{i}      {i**2}       {i**3}       {2**i}")

first = 'Bill'
Last = 'Gates'
print(f"{first} {Last}")

print('{:}'.format(1000/3))

def growthrates (n):
    'print values of below 3 function for i = 1, ..., n '
    print(' i      i**2     i**3    2**i')
    formatStr = '{0:2d}  {1:6d}  {2:6d}  {3:6d}'
    for i in range (2, n+1):
        print(formatStr.format(i, i**2, i**3, 2**i))
print(growthrates(20))

students = []
students.append(['Demoines', 'Jim', 'Sophomore', 3.45])
students.append (['Pierre', 'Sophie', 'Sophomore', 4.0])
students.append(['Columbus', 'Maria', 'Senior', 2.5])
students.append (['Phoenix', 'River', 'Junior', 2.45])
students.append(['Olympis', 'Edger', 'Junior', 3.99])
print((students))


print('{:8.5}'.format(1000/3))

n = 10
print('{:b}'.format(n))
print('{:c}'.format(n))
print('{:d}'.format(n))
print('{:x}'.format(n))

import time
print(time.time())

print(time.gmtime(0))

print(time.localtime())

print(time.strftime('%A %b %d %y %I: %M %p',time.localtime()))

#                        PROGRAMMING EXERCISE:

import time
print(time.strftime('%A, %b %d %y '))
print(time.strftime('%I:%M %p' ' Central Daylight Time on ' '%b %d %y'))


import time
var =  'It will be a sunny day today'
print(time.strftime ('It will be a sunny %A today'))
# print(time.strftime("It wll be a sunny %A today"))
count = var.count('day')
print(count)
weather = var.find('sunny')
print(weather)
change = var.replace('sunny','cloudy')
print(change)


first = 'john'
Last = 'Deo'
street = 'Main street'
number = 123
city = 'Anycity'
state = 'AS'
zip_code = '09867'
print('{:5}{:10}'.format(first,Last))
print('{:5}{:10}'.format(street,number))
print('{:7} {:6}{}'.format(city,state,zip_code))

var = 'The secret of this message is that it is secret.'
print(len(var))
count = var.count('secret')
print(count)
change = var.replace('secret', 'xxxxxx')
print(change)
print(var)


def month (n):
    if n == 1:
        return 'Jan'
    if n == 2:
        return 'Feb'
    if n == 3:
        return 'Mar'
    if n == 4:
        return 'Apr'
    if n == 5:
        return 'May'
    if n == 6:
        return 'Jun'
    if n == 7:
        return 'Jul'
    if n == 8:
        return 'Aug'
    if n == 9:
        return 'Sep'
    if n == 10:
        return 'Oct'
    if n == 11:
        return 'Nov'
    if n == 12:
        return 'Dec' 
print(month(8))

def cheer (n):
    print(f'How do you spell winner? \n I know, I know! \n {n.upper ()} \n And thats how you spell winner! \n Go Uitians' )
print(cheer("uitians"))


