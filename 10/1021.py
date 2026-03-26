''' 10/21/25 warmup
p = int(input("enter principle value"))
r = float(input("enter rate value"))
t = int(input("enter number of years"))
si = (p * t * (r*100))
print(f"calculated simple interest is", si) 
'''
''' grading system
grade = int(input("enter your numerical grade"))
if grade >= 90:
    print(grade, "is an A")
elif grade >=80 and grade <90:
    print(grade, "is a B")
elif grade >=75 and grade <80:
    print(grade, "is a C")
elif grade >=70 and grade <75:
    print(grade, "is a D")
else:
    print(grade, "is a F")
'''
''' Analyze a character to determine if the character is lowercase, uppercase, or a digit.
char = input("enter your character ")
val = ord(char)
if val>=65 and val<=90:
    print(char, "is an uppercase letter.","ASCII ==", val)
elif val>=97 and val<=122:
    print(char, "is a lowercase letter.","ASCII ==", val)
elif val>=48 and val<=57:
    print(char, "is a digit.","ASCII ==", val)
else:
    print("your charcter is not a digit, uppercase or lowercase letter")
'''

elec = float(input("input numerical value of electricty unit charges "))
price = float("")
if elec <= 50:
    price = ("price is", elec*0.50)
elif elec > 50 and elec <= 150:
    price = ("price is", ((elec-50)*0.70) + (elec*0.50))
elif elec > 150 and elec <= 250:
    price = ("price is", ((elec-150)*1.20) + ((elec-50)*0.70) + (elec*0.50))
else:
    price = ("price is", (elec-250)*1.50) +((elec-150)*1.20) + ((elec-50)*0.70) + (elec*0.50)

print("an additional surcharge of 20 percent is added to the bill, you're total electricty bill is", price)

'''
angleOne = float(input("enter your first triangle angle "))
angleTwo = float(input("enter your second triangle angle "))
angleThree = float(input("enter your third triangle angle "))
if (angleOne+angleTwo+angleThree) == 180:
    print("your triangle is valid")
else:
    print("your triangle is not valid")
'''
'''
num1 = float(input("enter number #1 "))
num2 = float(input("enter number #2 "))
num3 = float(input("enter number #3 "))

if num1 < num2 < num3:
    print("your numbers are increasing")
elif num1 > num2 > num3:
    print("your numbers are decreasing")
else:
    print("you numbers are not increasing or decreasing")
    '''
'''
days = int(input("how many days past due is your book? "))
if days <= 5:
    print("you owe 50 paise")
elif days >=6 and days <=10:
    print("you owe one rupee")
elif days >=10 and days < 30:
    print("you owe 5 rupees")
else:
    print("YOUR MEMBERSHIP IS CANCELLED AND YOU OWE: 5 RUPEES")
'''