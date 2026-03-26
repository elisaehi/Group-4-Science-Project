# Armstrong Exercise 
'''
num = int(input("please enter your number: "))
n = num
length = len(str(num))
total = 0

while n > 0:
    digit = num % 10
    total = digit ** length
    n = n // 10

if total == num:
    print("this is an armstrong number")
else:
    print("this is not an armstrong number")
'''
'''
# Prime Number
n = int(input("please enter your number: "))

for i in range (1, n+1):
    if (n % i == 0) and (i!=n or i!=1):
        print("this is not a prime number")
    else:
        print("this is a prime number")
'''

# Fibbonaci Series
'''
a,b = 0,1
for i in range(2):
    print(a)
    a,b = b, b+a
'''
for i in range(6):
    print("*" * i)