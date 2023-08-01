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

var = 'The secret of this message is that it is secret.'
print(len(var))
count = var.count('secret')
print(count)
change = var.replace('secret', 'xxxxxx')
print(change)
print(var)