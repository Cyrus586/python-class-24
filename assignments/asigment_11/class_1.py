class Human:
    def brain(self):
        return "Thinking"
class Cow(Human):
    def brain(self):
        return "Closure"
class Goat(Human):
    def brain(self):
        return "Meow"

# polymorphism example 1

def make_sound(animal):
    return animal.brain()

cow = Cow()
goat = Goat()

print(make_sound(cow))
print(make_sound(goat))


# polymorphism example 2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
p1 = Point(1,2)
p2 = Point(28,12)

result = p1 + p2
print(f"Result: {result.x}, {result.y}")
