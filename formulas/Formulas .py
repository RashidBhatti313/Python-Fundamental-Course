a = int(input("Enter the value of a: "))
n = int(input("Enter the value of n: "))
d = int(input("Enter the value of d: "))
an = (a + (n - 1) *d)
print(an)


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
x1 = (-b + (b**2 - (4*a*c))**0.5)/(2*a)
x2 = (-b - (b**2 - (4*a*c))**0.5)/(2*a)
print(x1,x2) 

l = int(input("Enter the value of l: "))
w = int(input("Enter the value of w: "))
A = (l * w)
print(A) 

r = int(input("Enter the value of r: "))
h = int(input("Enter the value of h: "))
A = (2)*(3.14)*r*h + (2)*(3.14)*r**2
print(A)


a1 = int(input("Enter the value of a1: "))
n = int(input("Enter the value of n: "))
d = int(input("Enter the value of d: "))
an = (a1 + (n - 1)* d)
print(an)


#              FIRST LAW OF MOTION:
Vi = int(input("Enter the value of Vi: "))
a = int(input("Enter the value of a: "))
t = int(input("Enter the value of t: "))

def firstEquationOfMotion(a,t,Vi):
    Vf = (Vi + (a)*(t))
    return Vf
print(firstEquationOfMotion(a,t,Vi))


#                SECOND LAW OF MOTION: 
Vi = int(input("Enter the value of Vi: "))
t = int(input("Enter the value of t: "))
a = int(input("Enter the value of a: "))

def SecondEquationOfMotion(a,t,Vi):
    S = ((Vi)*(t) + 0.5* (a)*(t**2))
    return S
print(SecondEquationOfMotion(a,t,Vi))



#              THIRD LAW OF MOTION:
Vi = int(input("Enter the value of Vi: "))
Vf = int(input("Enter the value of Vf: "))

def ThirdEquationOfmotion(Vi,Vf):
    TwoaS = (Vi**2) - (Vf**2)
    return TwoaS
print(ThirdEquationOfmotion(Vi,Vf)) 


l = int(input ("Enter the value of l: "))
w = int(input ("Enter the value of w: "))
p = ((l + w) * 2)
print(p)

s = 2
r = 3.5
av = (s + r)/2
print(av)