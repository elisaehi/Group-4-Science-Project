'''
num1 = int(input("enter your first number"))
for i in range(1,11,1):
    print(f"{num1}*{i}", "=", f"{num1 * i}")
'''
'''
for i in range(1,11,1):
    print(i)

n = int(input("\nenter your number: "))
total=0
for i in range (1,(n+1),1):
    total=total+i
print(total)
'''
'''
string = input("enter your phrase / word / sentence")
for i in string:
    print (i)

for i in range(1,6,1):
    print(f"*" * i)
'''
'''
userValue = int(input("please enter a number for your range "))
total = 0
for i in range(6, userValue, 1):
   if (i%3==1) and (i%4==1) and (i%5==1) and (i%6==1):
      total += 1

print (total)
'''
'''
userInput = input("please enter your word: ")
flag = False
end = (len(userInput))

for i in range(0, end):
    if (userInput[0] == userInput[-i-1]):
        flag=True
    else:
        flag=False
        break
if flag==True:
    print("this is a palindrome")
else:
    print("this is not a palindrome")
'''
'''
num = int(input("please enter your number"))
sum=0
for i in range(1,num):
        if(num%i==0):
                sum+=i
if(sum==num):
    print("your number is a perfect number!")
else:
    print("your number is not a perfect number")
'''
'''
digit = input("please enter your digit")
for i in digit:
    r = i/10
    product *=
'''
num = int(input("please enter your number (EX: 45): "))
flag = False

for i in range(1,num,1):
    if (num%i==1) and (i!=(1 or num)):
        flag=False
    else:
        flag=True
        break
    
if flag==True:
    print("this is a prime number")
else:
    print("this is not a prime number")

