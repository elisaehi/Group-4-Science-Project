'''
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def getBalance(self):
        return self.balance
    def setBalance(self, amount):
        if amount >= 0:
            self.balance = amount
        else:
            print("invalid balance amount")
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount(5000)
account.setBalance(7000)
print(account.getBalance())
account.withdraw(3000)
print(account.getBalance())
'''

class Student:
    def __init__(self, marks):
        self.marks = marks
    def getMarks(self):
        return self.marks
    def setMarks(self, value):
        if value >= 0 and value <= 100:
            self.marks = value
        else:
            print("invalid marks")

s1 = Student(85)
print(s1.getMarks())

s1.setMarks(110)
s1.setMarks(95)
print(s1.getMarks())
