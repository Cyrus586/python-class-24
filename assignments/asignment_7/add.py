def add(num1,num2):
    return (num1 + num2)

def get_input():
    number_1 = float(input('Enter Your First Number '))
    number_2 = float(input('Enter Your Second Number '))
    print("The summed values = ", add(number_1, number_2))

get_input()

print()
# EXAMPLE 2

print('EXAMPLE 2')
def add2(n1, n2):
    n1 = input('Enter value 1 ')
    n2 = input('Enter Value 2 ')
    result1 = int(n1) + int(n2)
    print('The summed value is:', result1)
    
add2(10,20)


