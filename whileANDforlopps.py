'''
import random

x = random.randint(0,50)
count = 0
userGuess = ""
while userGuess!=x:
    count+=1
    userGuess = int(input("\nPLEASE GUESS THE NUMBER BETWEEN 1 & 50: "))
else:
    print(f"YAY! you have correctly guessed the number, {x}! It took you {count} tries")
'''
'''
i = 1
while i < 10:
    print (i)
    i+=2
'''
'''
palindrome = input("please enter the word you would like to be checked: ")
flag = True

if palindrome != palindrome[::-1]:
    flag = False
    print("this is not a palindrome")
else:
    print("this is a palindrome")
'''



















'''
message = input("\nENTER THE MESSAGE YOU WISH TO BE ENCODED/DECODED: ").lower()
shift = int(input("\nENTER THE NUMBER YOU WANT YOUR MESSAGE TO BE ENCODED/DECODED WITH: "))
output = ""
for i in range(0,len(message)):
    shift = shift % len(message)
    output = message[-shift:] + message[:-shift]
print(output)
'''
'''
product = 1
num = int(input("please enter the number you want to multiply the digits of: "))

for i in str(num):
    product *= int(i)
print (product)
'''
'''
num = [9,50,36,18,3,88,-1,12,45,94,67,0]
for i in num:
    if i < 0:
        break
print(i)
'''

print (10>9)