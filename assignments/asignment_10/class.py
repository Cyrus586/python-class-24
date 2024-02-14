
print("------------------------------")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and i am {self.age} yrs old. "
    
    @property
    def is_adult(self):
        return self.age >= 18
    
    def celebrate(self):
        self.age += 1

my_self = Person("Aksam",25) # object

# accessing properties
print(my_self.name)
print(my_self.age)


# calling methods
print(my_self.greet())
print(my_self.is_adult)
my_self.celebrate()
print(my_self.age)
print(my_self.is_adult)

print("------------------------------")


class Car(Person): # inheritance
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
        
    def start_engine(self):
        self.is_running = True
        print("The car engine has started")
        print(self.is_running)
    
    def stop_engine(self):
        self.is_running = False
        print("The car engine has stoped")
        print(self.is_running)


make = str(input("Please enter car make: "))
model = str(input("Please enter car model: "))
year = int(input("Please enter car year: "))

my_car = Car(make, model, year)
print(my_car.start_engine())
print(my_car.stop_engine())
