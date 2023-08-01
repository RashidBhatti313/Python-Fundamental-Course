import time
print(time.time())

print(time.gmtime(0))

print(time.localtime())

print(time.strftime('%A %b %d %y %I: %M %p',time.localtime()))


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