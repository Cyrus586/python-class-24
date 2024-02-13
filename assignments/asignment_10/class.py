

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"hello, my name is {self.name} and i am {self.age} yrs old. "
    
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
