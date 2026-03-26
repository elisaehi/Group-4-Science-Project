'''
word = "racecar"
def palindromFunction(word):
    for i in range(0, len(word)):
        if word[i] == word[-i-1]:
            print(f"{word} is a palindrome")
        else:
            print("this is not a palindrome")
'''




count = 0

def countOddDigits(num):
    global count
    while num > 0:
        digit=num%10
        #print(digit)
        if (digit % 2 != 0):
          count += 1
        num //= 10
        
    return (count)
   # print(f"there are {count} odd numbers")

print(countOddDigits(16432))