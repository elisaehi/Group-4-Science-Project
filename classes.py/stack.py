'''
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack")

    def pop(self):
        if len(self.stack) == 0:
            print("stack underflow")
        else:
            removed = self.stack.pop
            print(f"{removed} popped from stack")
        return removed
    
    def peek(self):
        if len(self.stack) == 0:
            print("stack is empty")
        else:
            return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def display(self):
        print("stack elements:", self.stack)


s = Stack()
s.push(19)
s.push(20)
s.push(188)

s.display()
print("top element:", s.peek())
s.pop()
s.display()
'''

class Daisy:

    def __init__(self):
        self.Q1 = []
        self.Q2 = []
        self.Q3 = []
        self.Q4 = []

    def push(self, iD):
        quardantNum = input("please enter what qudrant you would like to access: ")

        if quardantNum == 1:
            self.Q1.append(iD)
            print(self.Q1)
        elif quardantNum == 2:
            self.Q2.append(iD)
            print(self.Q2)
        elif quardantNum == 3:
            self.Q3.append(iD)
            print(self.Q3)
        else:
            self.Q4.append(iD)
            print(self.Q4)

        print(f"Daisy #{iD} from qudrant {quardantNum} was pushed to stack.")

    def pop(self):
        quardantNum = input("please enter what qudrant you would like to access: ")

        if quardantNum == 1 and len(self.Q1) != 0:
            self.Q1.pop()
            print(self.Q1)
        elif quardantNum == 2 and len(self.Q1) != 0:
            self.Q2.pop()
            print(self.Q2)
        elif quardantNum == 3 and len(self.Q1) != 0:
            self.Q3.pop()
            print(self.Q3)
        elif quardantNum == 4 and len(self.Q1) != 0 :
            self.Q4.pop()
            print(self.Q4)
        else:
            print("ERROR: stack underflow")
        
    def peek(self):
        quardantNum = input("please enter what qudrant you would like to access: ")

        if quardantNum == 1 and len(self.Q1) != 0:
            self.Q1[-1]
            print(self.Q1)
        elif quardantNum == 2 and len(self.Q1) != 0:
            self.Q2[-1]
            print(self.Q2)
        elif quardantNum == 3 and len(self.Q1) != 0:
            self.Q3[-1]
            print(self.Q3)
        elif quardantNum == 4 and len(self.Q1) != 0 :
            self.Q4[-1]
            print(self.Q4)
        else:
            print("ERROR: stack underflow")
    
    def display(self):
        quardantNum = input("please enter what qudrant you would like to access: ")

        if quardantNum == 1 and len(self.Q1) != 0:
            print(self.Q1)
        elif quardantNum == 2 and len(self.Q1) != 0:
            print(self.Q2)
        elif quardantNum == 3 and len(self.Q1) != 0:
            print(self.Q3)
        elif quardantNum == 4 and len(self.Q1) != 0 :
            print(self.Q4)
        else:
            print("there is nothing in this list")

d = Daisy()
d.push(2)
d.push(15)
d.peek()
d.display()