a = 400
b = 500
if a == 400:
    print("The value of a is equal to 400 ")
if a < b:
    print("The value of a is less to b ")
if a > b:
    print("The value of a is greater than b ")

a = 500
b = 400
if a != b:
    print("The value of is equal to 500 ")
if a <= b:
    print("The value of is less or equal to than b ")
if a >= b:
    print("The value of is greater or equal to than b ")


a = 10
b = 5
c = 20
if a>b and c>b:
    print("Both condition are True")

l_limit = int(input("Enter lower limit range: "))
u_limit = int(input("Enter upper limit range: "))
print("Prime number between",l_limit and u_limit)
for number in range(l_limit,u_limit+1):
    if number > 1:
        for i in range(2,number):
            if(number%i) == 0:
                break
        else:
             print(number)


initial_value = eval(input("Enter the initial value for range: "))
final_value = eval(input("Enter the final value for range: "))
numbers = range(initial_value,final_value)
sum = 0
for value in numbers:
    sum = sum+value
print("The sum is", sum)       


