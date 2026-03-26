''' square root calculator
import math
num = int(input("\nplease input the number you want to find the square root of: "))
print(math.sqrt(num))
'''
''' compound interest calculator
import math
principal = int(input("enter the principal amount: "))
rate = int(input("enter the percent interest rate number: "))
time = int(input("enter the number of years: "))
total = principal * math.pow(1 + (rate/100), time)
print("the total amount is", int(total), "dollars")
'''
'''
import math
num = float(input("enter you number "))
print("the smallest integer that is greater than or equal to your number is ", math.ceil(num))
print("the largest integer that is less than or equal to your number is ", math.floor(num))
print("your number rounded to the tenth decimal place is ", round(num,2))
'''
'''
import math
num = int(input("enter you number: "))
print("the greatest common divisor (GCD) of your nymber is: ", math.gcd(num))
print("the factorial of your number is: ", math.factorial(num))
'''
'''
import math
num1 = int(input("enter your first number please: "))
num2 = int(input("enter your second number please: "))
operation = input("please choose an operation(square root/power/sine/log) as provided: " \
'''
'''
email = input("\nenter your email: ")
if ("@" in email) and (email.endswith(".com") and email.endswith(".org"))
    print ("your email is valid")
else:
    print("your email is not valid please enter a new one")
'''
'''
url = input("please enter your URL")
url = url.replace("https://", "").replace("www.", "")
domain = url.split("/")[0]
print("your domain is:", domain)
'''
'''
sentence = input ("enter your sentence: ")
words = sentence.split
titleWords = []

for words in words:
    if len(words) > 0:
        newWord = words[0].upper() + words[1:].lower()
        titleWords.append(newWord)
    else:
        titleWords.append(words)
'''
'''
paragraph = input("enter your paragraph")
for p in [",",".", "!", "?", ";",":"]:
    paragraph = paragraph.replace(p, "")
words = paragraph.lower().split()
uniqueWords = set(words)
print("unique words:", len(uniqueWords))
'''
'''
text = input("please enter your text: ")
text =  text.replace("btw", "by the way")
text =  text.replace("idk", "i don't know")
text = text.replace("omw", "on my way")
print("output: ", text)
'''
i = 0
while i <5:
    print(str(i)*i)
    i+=1