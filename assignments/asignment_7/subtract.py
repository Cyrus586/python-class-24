# EXAMPLE 1
def subract(number_1, number_2):
    number_1 = float(input('Enter Your First Number '))
    number_2 = float(input('Enter Your Second Number '))
    result = float(number_1) - float(number_2)
    return (result)


print()
def outPut():
    print("The subtracted values = ", subract(10,20))

outPut()



print()
# EXAMPLE 2

print('EXAMPLE 2')

def subracted(num1,num2):
    return (num1 - num2)

def get_input():
    number_1 = float(input('Enter Your First Number '))
    number_2 = float(input('Enter Your Second Number '))
    print("The subtracted values = ", subracted(number_1, number_2))

get_input()