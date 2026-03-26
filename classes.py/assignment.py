'''
def bookSearch(bookIds, target):
    for book in bookIds:
        if book == target:
            return True
    return False


listofBooks = [123, 55, 450, 100, 7, 23]
searchId = 100

if bookSearch(listofBooks, searchId):
    print("This specefic book ID exists in the system")
else:
    print("Book ID is not found.")
'''
'''
def studentRoll(studentRollNumbers, target):
    low = 0
    high = len(studentRollNumbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if studentRollNumbers[mid] == target:
            return True
        elif studentRollNumbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

studentRollNumbers = [1001, 1002, 1003, 1004, 1005, 1006]
choice = 1004

if studentRoll(studentRollNumbers, choice):
    print("Valid roll number.")
else:
    print("Invalid roll number.")
'''
'''s
def orderSystem(orders, target):
    for order in orders:
        if order == target:
            return True
    return False

dailyOrders = [4501, 4502, 4503, 4504, 4505]
particularOrder = 4503

if orderSystem(dailyOrders, particularOrder):
    print("The order was placed today!")
else:
    print("Order not found")
'''
'''
def gameChecker(scores, target):
    low = 0
    high = len(scores) - 1

    while low <= high:
        mid = (low + high) // 2

        if scores[mid] == target:
            return True
        elif scores[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

leaderboard = [100, 200, 350, 273, 750, 1000]
score = 500

if gameChecker(leaderboard, score):
    print("The score already exists on the leaderboard")
else:
    print("The score cannot be found on the leaderboard.")
'''
'''
def attendanceSystem(ids, target):
    for i in ids:
        if i == target:
            return True
    return False

attendanceIds = [123, 55, 976, 382, 15]
studentId = 111

if attendanceSystem(attendanceIds, studentId):
    print("This student's ID was scanned")
else:
    print("This student's ID was not scanned")
'''
'''
def searchBook(fileName, target):
    with open(fileName, "r") as file:
        for line in file:
            if int(line.strip()) == target:
                return True
    return False


bookId = 221

if searchBook("books.txt", bookId):
    print("Book found.")
else:
    print("Book not found.")
'''
'''
bookIds = [279, 192, 531, 221, 678, 270]

with open("books.txt", "w") as file:
    for i in bookIds:
        file.write(str(i) + "\n")

def searchBook(fileName, target):
    with open(fileName, "r") as file:
        for line in file:
            if int(line.strip()) == target:
                return True
    return False


bookId = 221

if searchBook("books.txt", bookId):
    print("THE BOOK IS IN THE LIBRARY!")
else:
    print("SORRY, THE BOOK COULD NOT BE FOUND")


rollNumbers = [1001, 1002, 1003, 1004, 1005, 1006]

with open("rolls.txt", "w") as file:
    for i in rollNumbers:
        file.write(str(i) + "\n")
'''

def rollNumbers(fileName, target):

    with open(fileName, "r") as file:
        numbers = [int(line.strip()) for line in file]

    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == target:
            return("validated")
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return("not validated")


if rollNumbers("rolls.txt", 762):
    print("The roll number is validated")
else:
    print("The roll number not found.")