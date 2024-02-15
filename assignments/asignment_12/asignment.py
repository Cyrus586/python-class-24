# Encapsulation: Refers to the bundling of data(attributes) and methds(functions) that operate on the data into a single unit,typically a class

class BankAccount():
    def __init__(self, account_number, balance):
        self._account_number = account_number # encapsulated attribute
        self._balance = balance # encapsulated attribute
        
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds")

balance = int(input("Enter bank balance: "))
account_num = int(input("Enter bank account number: "))
account1 = BankAccount(account_num, balance)


# Abstraction: refers to the process of hiding complex implementation details and showing only the essential features of an oblect

from abc import ABC, abstractmethod

class Shape(ABC):
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

rectangle = Rectangle(5,4)
circle = Circle(3)

print("Area of a rectangle", rectangle.area())
print("Area of a circle", circle.area())
        