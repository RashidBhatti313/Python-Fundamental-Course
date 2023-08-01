def alleven(x):
    i = 0
    re = True
    while(i<= len(x)):
        if i%2 == 0:
            return re
        i +=1
    return False
print(alleven([2,4,6,8]))

def alleven(x):
    i = 0
    re = False
    while(i<= len(x)):
        if i%2 == 0:
            return re
        i +=1
    return True
print(alleven([2,3,4,5,6]))
#                               PRACTICE PROBLEM 3.12:




#                                   [LECTURE 03: ]
def f(x):
    res = x**2 + 1
    return res

print(f(4))


def dum(x,e,r,y):
    return x+e+r+y
print(dum(5,5,6,5))

def squareSum(x, y):
    return x**2 + y**2
print(squareSum(5,7))


def hello(name):
     print('Hello'+name +'!')
hello("Rashid")

def f(x):
    print(x**2+1)


s =input("Enter the square or Cube: ")
if s == 'square':
    def f(x):
        return x*x
    print(f(2))
else:
    def f(x):
        return x*x*x
    print(f(3))

def f(x):
    return x**2+1
print(f(3))

def g(x):
    return f(x)
def f(x):
    return x**3

print(g(4))

def g(y):
    return f(y)
def f(x):
    return x**2+1

print(f(4)) 

def f(x):
    res = x**2+1
    return res
print(f(3))

def g(x):
    res = x**3+1
    return res 
print(g(4))