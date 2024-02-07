from datetime import datetime

# EXAMPLE 1
def helloWorld():
    print("Hello World")

helloWorld()

# EXAMPLE 2
def time():
    current_time = datetime.now().strftime('%H:%M:%S')
    print('Current time:', current_time)

time()


# EXAMPLE 3

def add(item1, item2):
    result = item1 + item2
    print(result)
    
add(17, 10)
add('Hello ', 'World')


def Name(): 
    name = input('Enter your Name?: ') 
    return name  




def Age(): 
    age = input('Enter your age?: ') 
    print(Name(), age)
    
Age()

