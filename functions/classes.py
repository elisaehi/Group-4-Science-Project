'''
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def introduce(self):
        print(f'Hi, I am {self.name} and I stidy in Grade {self.grade}.')

    def upgradeGrade(self):
        self.grade += 11
        print(f"{self.name} has been promoted to Grade {self.grade}!")

student1 = Student("aarav", 10)
student2 = Student("mia", 11)

print(student1.name)
print(student2.grade)

student1.introduce()
student2.introduce()

student1.upgradeGrade()
student2.upgradeGrade()
'''
'''
class superhero:
    def __init__(self, name, power, color, city):
        self.name = name
        self.power = power
        self.color = color
        self.city = city

    def introducton(self):
        print(f"Hello! My name is {self.name} and I protect {self.city}. I have the power of {self.power} and my favorite color is{self.color}!")


superhero1 = superhero()
'''

'''
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def getPerimeter(self):
        return 2 * self.length + 2 * self.width

length = float(input("enter the length of the rectangle: "))
width = float(input("enter the width of the rectangle: "))
myRectangle = rectangle(length, width)
print("the perimeter of the rectangle is:", myRectangle.getPerimeter())
'''
'''
class trapezoid:
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def getArea(self):
        return 0.5 * (self.base1 + self.base2) * self.height

base1 = float(input("enter the area of base #1: "))
base2 = float(input("enter the area of base #2: "))
height = float(input("enter the height: "))
myTrapezoid = trapezoid(base1, base2, height)
print("the area of the trapezoid is:", myTrapezoid.getArea())
'''
'''
class cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def getVolume(self):
        return (1/3) * (22/7) * ((self.radius)**2)  * self.height

radius = float(input("enter the radius length: "))
height = float(input("enter the height: "))

myCone = cone(radius, height)
print("the volume of the cone is:", myCone.getVolume())
'''
'''
class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "available" 

    def borrowBook(self):
        if self.status == "available":
            return self.status == "borrowed"
        else:
            print(f"sorry,{self.title} is already borrowed")
    def returnBook(self):
        if self.status == "borrowed":
            return self.status == "available"
        else:
            print(f"{self.title} has already been returned")
    def getInfo(self):
        print(f"{self.title} is {self.status}")

book1 = book("harry potter","jk rowling")

book1.getInfo()

book1.borrowBook()
book1.getInfo()
book1.returnBook()
book1.getInfo()
'''
'''
class vehicle:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount 
    def brake(self, amount):
        if amount < self.speed:
            self.speed -= amount
        else:
            self.speed = 0
  
    def getInfo(self):
        print(f"the make is {self.make}, the model is {self.model}, the year it was made was {self.year}, and the current speed is {self.speed}")



car = vehicle("Toyota", "Corolla", 2020, 0)
car.getInfo() # Toyota Corolla (2020) - Speed: 0 km/h
car.accelerate(50)
car.getInfo() # Toyota Corolla (2020) - Speed: 50 km/h
car.brake(20)
car.getInfo() # Toyota Corolla (2020) - Speed: 30 km/h
car.brake(40)
car.getInfo() # Toyota Corolla (2020) - Speed: 0 km/h
'''

class sortProj:

    def __init__(self, list):
        self.list = list

    def bubbleSort(self):
        for i in range(len(list)):
            for j in range(0,len(list) - i - 1):
                if list[j] > list [j+1]:
                    temp = list[j]
                    list[j] = list[j+1]
                    list[j+1] = temp

list = float(input("please enter your list: "))