'''RIGHT ANGLED TRIANGLE CALC 
base = float(input("enter the base "))
height = float(input("enter the height "))
area = base * height * 0.5
print(area)
'''
'''  PRINT THE SUM OF 3 DIGITS 
number = input("enter your three digit number ")
firstNum = int(number[0])
secondNum = int(number[1])
thirdNum = int(number [2])
print("the sum of your three digits are",(firstNum + secondNum + thirdNum))
'''
'''SWAP TWO DIGITS
num = input("enter your two digit number")
firstDigit = int(num[0])
secondDight = int(num[1])
print(f"{num[1]}{num[0]}")
'''
'''YEAR TO CENTURY
year = (input("enter the year"))
century = int(year[0:2])
finalCentury = (century + 1)
if year[2:4] == "00":
    print(f"{year[0:2]}","century")
else:
    print(f"the year", year, "is in the", finalCentury, "century")
'''

time = int(input("enter the number of seconds since midnight"))
hours = str(time/3600)
hours1 = str({hours[0:2]})
hours2 = str({hours[2:5]})
print(f"{hours[0:2]}","the time is", "{hours[]}")