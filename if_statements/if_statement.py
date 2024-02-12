a = int(input("Enter first value: "))
b = int(input("Enter first value: "))
print("-------------------------")


def add(a,b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer))

def subtract(a,b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer))

def divide(a,b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer))

def multipy(a,b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer))

choice = input("Enter your choice: ")
print("A, Addition")
print("B, Subtraction")
print("C, Multiplication")
print("D, Divition")


if choice == "a" and choice == "A":
    print("Addition")
    add(a,b)

elif choice == "b" or choice == "B":
    print("Subtraction")
    subtract(a,b)
elif choice == "c" or choice == "C":
    print("Multiplication")
    multipy(a,b)
elif choice == "d" or choice == "D":
    print("Division")
    divide(a,b)


else:
    print("Come on pick one of the choices above", choice)



