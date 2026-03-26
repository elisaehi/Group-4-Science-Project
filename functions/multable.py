
def changeNumber(x):
    x = x+5
    print("inside function: ", x)

num = 10
changeNumber(num)
print("Outside function: ", num)
'''
# pass by value
'''
def modifyList(lst):
    lst.append(100)
    print("inside function: ", lst)

numbers = [1,2,3]
modifyList(numbers)
print("outside function: ", numbers)
'''
# pass by reference

'''
def reassignList(lst):
    lst =[0,0,0]
    print("inside function: ", lst)

numbers = [1,2,3]
reassignList(numbers)
print("outside function: ", numbers)
'''
# reassigning the value
'''
def getScores():
    scores = []
    while True:
        score = input("enter a quiz score (or 'done' to finish): ")
        if score.lower() == "done":
            break
        scores.append(float(score))
    return scores

def average(scores):
    sum = 0
    for i in scores:
        sum += i

    return sum / len(scores)

def highest(scores):
    highestScore = scores[0]
    for i in scores:
        if i > highestScore:
            highestScore = i
    return(highestScore)
           
def lowest(scores):
    lowestScore = scores[0]
    for i in scores:
        if i < lowestScore:
            lowestScore = i
    return(lowestScore)

def countPassed(scores, passingMark):
    count = 0
    for i in scores:
        if i >= passingMark:
            count += 1
    return count

scores = getScores()
if len(scores) == 0:
    print("no scores entered. ")
else:
    avg = average(scores)
    high = highest(scores)
    low = lowest(scores)
    passed = countPassed(scores, 50)

    print("\nquiz score report")
    print("-------------------")
    print("scores:", scores)
    print(f" average score: {avg:.2f}")
    print(f" highest score: {high}")
    print(f" lowest score: {low}")
    print(f" students passed: {passed}/{len(scores)}")
'''
'''
def displayMenu():
    print("------------------")
    print("    ATM Menu      ")
    print("------------------")
    print("would you like to check your balance? (1)")
    print("would you like to deposit money? (2)")
    print("would you like to withdraw money? (3)")
    print("i would like to exit (4)")

def checkBalance(balance):
    print("----------------------------------------")
    print(f"your balance is: ${balance:.2f}")
    print("----------------------------------------")
    return balance
    
def deposit(balance):
    depositAmount = float(input("enter deposit amount: "))
    if depositAmount > 0:
        balance += depositAmount
        print(f"${depositAmount:.2f} deposited")
    else:
        print("-------------------------")
        print(" invalid deposit amount. ")
        print("-------------------------")
    return balance

def withdraw(balance):
    withdrawAmount = float(input("enter withdrawal amount: "))
    if withdrawAmount <= 0:
        print("invalid withdrawal amount")
    elif withdrawAmount > balance:
        print("insufficent funds")
    else:
        balance -= withdrawAmount
        print("--------------------------------------")
        print(f"${withdrawAmount:.2f} withdrawn")
        print("--------------------------------------")
    return balance

balance = 0.0

while True:
    displayMenu()
    choice = input("choose an option (1-4): ")

    if choice == "1":
        balance = checkBalance(balance)
    elif choice == "2":
        balance = deposit(balance)
    elif choice == "3":
        balance = withdraw(balance)
    elif choice == "4":
        print("thank you for using the ATM!")
        break
    else:
        print("not a option, please input a correct number.")

