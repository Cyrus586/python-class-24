from datetime import datetime
def helloWorld():
    print("Hello World")

helloWorld()

def time():
    current_time = datetime.now().strftime('%H:%M:%S')
    print(f'Current time: {current_time}' )

time()

def add(item1, item2):
    result = item1 + item2
    print(result)
    
add(17, 10)
add('Hello ', 'World')
