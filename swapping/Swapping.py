# Swapping 

a = 6
b = 3
a,b = b,a 
print(a,b)
a = 'hello'
b = 3.2
c = (1,2,3,4)
d = ['JAN','FEB','MAR']
print(a,b,c,d)
a,b,c,d = d,c,b,a
print(a,b,c,d)

def g(x):
    x = 5
    return x
print(g(5))

def plus (a,b):
    print("You have entered the value of variable a: ", a)
    print("You have entered the value of variable b: ", b)
    print("Our plus operator with generate: ")
    return a+b
print(plus(3,5))

def g(x):
    x = 3
    return x
print(g(3))

mylist = [3,4,6,7,8]
def m_p (lst):
    lst [0] = 5
    return lst
print(m_p(5))

a = [5,6,7]
b = a
a = 3
print(a,b)