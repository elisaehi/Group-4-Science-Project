'''
file = open("notes.txt", "w")
file.write("Python File Handling Lab\n") 
file.write("This file stores student notes.\n") 
file.close() 
'''
'''
file = open("notes.txt", "r") 
content = file.read() 
print(content) 
file.close() 
'''
'''
file = open("notes.txt", "a") 
file.write("File handling allows data persistence.\n") 
file.close() 

import os # Used for checking if file exists for clarity

def addStudent(name):
    with open('attendance.txt', 'a') as file:
        file.write(name + '\n')
    print(f"Student '{name}' added successfully.")

def viewStudents():
    if not os.path.exists('attendance.txt') or os.path.getsize('attendance.txt') == 0:
        print("No students have attended yet.")
        return

    print("\n--- Current Attendance ---")
    with open('attendance.txt', 'r') as file:
        for line in file:
            print(line.strip())
    print("--------------------------")

while True:
    print("\nAttendance System Menu:")
    print("1. Add Student")
    print("2. View Attendance")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        student_name = input("Enter name to add: ")
        addStudent(student_name)
    elif choice == '2':
        view_students()
    elif choice == '3':
        print("Exiting system.")
        break
    else:
        print("Invalid choice, please try again.")
'''
'''
class ListAnalyzer:
    def __init__(self, dataList):
        self.dataList = dataList

    def noRepeats(self):
        return len(self.dataList) == len(set(self.dataList))

dataList1 = ListAnalyzer([-99,1,2,3,4,5,6,6,6,6,6,7,8,9,10,12345,5,5,5,5])
print(dataList1.noRepeats())
'''
'''

class listAnalyzer:
    def __init__(self, dataList):
        self.dataList = dataList

    def mostFrequent(self):
        for i in dataList:

        return set(self.dataList)

dataList1 = listAnalyzer([-99,1,2,3,4,5,6,6,6,6,6,7,8,9,10,12345,5,5,5,5])
print(dataList1.mostFrequent())
'''
'''

def addStudent(name):
    with open("attendance.txt", "a") as file:
        file.write(name + "\n")
    print("Student added successfully")

def view_students():
    with open("attendance.txt", "r") as file:
        for student in file:
            print(student.strip())

def add_student(name):
    with open("attendance.txt", "r") as file:
        students = file.read().splitlines()

    if name in students:
        print("Student already exists")
    else:
        with open("attendance.txt", "a") as file:
            file.write(name + "\n")
        print("Student added successfully")

from datetime import date

def add_student(name):
    today = date.today()
    with open("attendance.txt", "a") as file:
        file.write(f"{name} - {today}\n")

def search_student(name):
    with open("attendance.txt", "r") as file:
        for line in file:
            if name in line:
                print("Student found:", line.strip())
                return
    print("Student not found")

def view_students():
    with open("attendance.txt", "r") as file:
        for i, student in enumerate(file, start=1):
            print(f"{i}. {student.strip()}")


while True:
    print("1. Add Student")
    print("2. View Attendance")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        add_student(name)
    elif choice == "2":
        view_students()
    else:
        print("Invalid choice")
'''
'''
list  = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range (0,9):
    if list[i] == 20:
        print(list[i], "find the position: ", i+1)

print("END")
'''
'''
def linearSearch(bookIds, targetId):
    for index, book_id in enumerate(bookIds):
        if book_id == targetId:
            return f"Book ID {target_id} found at index {index}."
    return f"Book ID {target_id} not found."

# Example Usage:
library_books = [101, 205, 87, 342, 55, 999]
target = 87
print(f"Scenario 1: {linear_search(library_books, target)}")
target_not_found = 500
print(f"Scenario 1: {linear_search(library_books, target_not_found)}")


def binary_search(roll_numbers, target_roll):
    """Searches for a target roll number in a sorted list."""
    left, right = 0, len(roll_numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if roll_numbers[mid] == target_roll:
            return f"Roll number {target_roll} is valid."
        elif roll_numbers[mid] < target_roll:
            left = mid + 1
        else:
            right = mid - 1
    return f"Roll number {target_roll} is invalid."

# Example Usage:
sorted_roll_numbers = [1001, 1005, 1010, 1015, 1020, 1025]
target = 1015
print(f"Scenario 2: {binary_search(sorted_roll_numbers, target)}")
target_not_found = 1012
print(f"Scenario 2: {binary_search(sorted_roll_numbers, target_not_found)}")

def find_order(order_list, order_number):
    """Checks if a specific order number is in the daily orders list."""
    for order in order_list:
        if order == order_number:
            return f"Order #{order_number} was placed today."
    return f"Order #{order_number} not found in today's records."

# Example Usage:
today_orders = [5001, 5002, 5005, 5010, 5012]
target_order = 5005
print(f"Scenario 3: {find_order(today_orders, target_order)}")

def check_score_exists(leaderboard, new_score):
    """Uses binary search to efficiently check if a score exists."""
    left, right = 0, len(leaderboard) - 1
    while left <= right:
        mid = (left + right) // 2
        if leaderboard[mid] == new_score:
            return f"Score {new_score} already exists on the leaderboard."
        elif leaderboard[mid] < new_score:
            left = mid + 1
        else:
            right = mid - 1
    return f"Score {new_score} is new and can be added."

# Example Usage:
sorted_scores = [100, 250, 400, 550, 700, 900]
score_to_check = 400
print(f"Scenario 4: {check_score_exists(sorted_scores, score_to_check)}")
'''
'''
def swap(a,b):
    a,b = b,a

def bubbleSort(dailySale, days):
    n = len(dailySale)
    for i in range(n-1):
            for j in range(0,(n-1)-i):
                if dailySale[j] > dailySale[j+1]:
                    dailySale[j], dailySale[j+1] = dailySale[j+1], dailySale[j]
                    days[j], days[j+1] = days[j+1], days[j]
    return days, dailySale

dailySale = [20, 55, 100, 150, 32, 99, 45]
days = ["mon", "tues", " wed", "thurs", "fri", "sat"]

print(bubbleSort(dailySale, days))
'''
'''
def linearSearch(data, target):
    for index in range(len(data)):
        if data[index] == target:
            return index 
    return -1 


bookIds = [7345, 1290, 9812, 2045, 5678]
searchId = 2045
resultIndex = linearSearch(bookIds, searchId)

if resultIndex != -1:
    print(f"Book ID {searchId} found at index: {resultIndex}")
else:
    print(f"Book ID {searchId} not found")

def loadIdsFromFile(filename):
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f.readlines()]

fileBookIds = loadIdsFromFile('book_ids.txt')

def binarySearch(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid 
        elif data[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1 
    return -1


rollNumbers = [1001, 1045, 1102, 1240, 1357, 1490] 
searchRoll = 1240
resultIndex = binarySearch(rollNumbers, searchRoll)

if resultIndex != -1:
    print(f"Roll number {searchRoll} found at index: {resultIndex}")
else:
    print(f"Roll number {searchRoll} not found")

def load_sorted_rolls_from_file(filename):
    with open(filename, 'r') as f:
        return sorted([int(line.strip()) for line in f.readlines()]) 
'''
'''
students = ["Ayaan", "Riya", "Neha"]
with open("students.txt", "w") as file:
    for name in students:
        file.write(name + "\n")

newList = []
with open("students.txt", "r") as file:
    for line in file:
        newList.append(line.strip())
print(newList)

def addStudent(name):
    with open("attendance.txt", "a") as file:
        file.write(name + "\n")
    print("Student added successfully")

def viewStudents():
    try:
        with open("attendance.txt", "r") as file:
            print("--- Attendance List ---")
            print(file.read())
    except FileNotFoundError:
        print("No attendance records found.")

# Simple Menu
while True:
    print("\n1. Add Student\n2. View Attendance\n3. Exit")
    choice = input("enter choice: ")
    if choice == '1':
        name = input("enter name: ")
        addStudent(name)
    elif choice == '2':
        viewStudents()
    elif choice == '3':
        break
'''
'''

def findSmallestinFile(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            
            if not lines:
                print("File is empty.")
                return

            count = int(lines[0].strip())
            smallest = int(lines[1].strip())
            
            
            for i in range(2, count + 1):
                value = int(lines[i].strip())
                if value < smallest:
                    smallest = value
            
            print(f"The smallest value in the file is :: \"{smallest}\"")

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")


with open("input.dat", "w") as f:
    f.write("5\n10\n-5\n-28184\n100\n50")


findSmallestinFile("input.dat")

def sumValuesinFile(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            
            if not lines:
                print("File is empty.")
                return

            count = int(lines[0].strip())
            total = 0
            
            for i in range(1, count + 1):
                total += int(lines[i].strip())
            
            print(f"The total sum of values is :: \"{total}\"")

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")


with open("data.txt", "w") as f:
    f.write("4\n10\n20\n30\n40")


sumValuesinFile("data.txt")

def mergeSalesData():
    names = []
    sales = []
    max_records = 1000

    try:
        with open("names.txt", "r") as f_names, open("sales.txt", "r") as f_sales:
            for line_n, line_s in zip(f_names, f_sales):
                if len(names) < max_records:
                    names.append(line_n.strip())
                    sales.append(line_s.strip())
                else:
                    break
        
        with open("merge.txt", "w") as f_merge:
            for i in range(len(names)):
                f_merge.write(f"{names[i]} {sales[i]}\n")
        
        print("Data merged successfully into merge.txt")

    except FileNotFoundError:
        print("Error: One or more files not found.")

with open("names.txt", "w") as f:
    f.write("Amina\nCarlos\nEmily\nHao\nIsabella")
with open("sales.txt", "w") as f:
    f.write("23424\n42549\n52488\n37562\n44770")

# Run the function
mergeSalesData()
'''

'''
def namesAndGrades(arr,n):
    for i in range(1, n):
        for j in range(0, n-2):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return(arr)

n = 4
grades = [78, 88, 92, 65]

arr = ["Ali", "Noor", "Sara", "Usman"]
arr = namesAndGrades(arr,n)

for i in range(n):
    print(arr[i], grades[i])

for i in range (0, n-2):
    if i 
sorted
'''

count = 0
files = "text.txt"

with open("text.txt", "w") as file:
            file.write("hello word my name is elisa")
with open("text.txt", "r") as file:
            lines = file.readlines()
            
for i in str(lines):    
        if i in lines:
            count[i] += 1
print(i, count)

'''

def ceaserCipher(files, num):

    files = "secret.txt"

    with open("secret.txt", "w") as file:
            file.write("meridian")
    with open("text.txt", "r") as file:
            lines = file.readlines()

    for i in lines:
'''

