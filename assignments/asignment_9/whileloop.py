# EXAMPLE 1
def Checking_num():
    numbers = [1,2,3,4,5,6]
    counter = 0 # responsible for counting the even or odd nums
    while counter < len(numbers):
        # using an if statement to check if the current is even
        if numbers[counter] % 2 == 0: # this is the even if statement which checks if there are numbers that can be divisable by 2 
            print(f"{numbers[counter]} is even")
        else:
            print(f"{numbers[counter]} is odd") # this else automatically 
        counter += 1
    # end while
    print("----------------------------------")
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
            
Checking_num()



# EXAMPLE 2
def vowels():
    students = ["Panchal", "Joel", "Rajvir", "Emma", "Afford", "Mumbere", "Aksam"]
    index = 0

    while index  < len(students):
        # using an if statement to check if the current element starts with a vowel
        if students[index][0].lower() in ["a","e","i","o","u"]:
            print(f"{students[index]} starts with a vowel")
        else:
            print(f"{students[index]} does not starts with a vowel")
        index += 1
        

    print("------------------------")

    for student in students:
        # using an if statement to check if the current element ends with a vowel
        if student[-1].upper() in ["a","e","i","o","u"]:
            print(f"{student} ends with a vowels")
        else:
            print(f"{student} does not ends with a vowels")
vowels()   

# EXAMPLE 3
def fruit_leng():
    fruits = ["apple","banana","orange","mango","Kiwi"]
    count = 0
    print("----------------------------------")
    print("using a while loop:")

    while count < len(fruits):
        if len(fruits[count]) % 2 == 0:
            print(f"The Length of {fruits[count]} is a even number")
        elif len(fruits[count]) % 2 != 0:
            print(f"The Length of {fruits[count]} is a odd number")
        else:
            print(f"The Length of {fruits[count]} is unkwon")
        count += 1


    print("----------------------------------")
    print("\nusing a for loop:")
    for fruit in fruits:
        if len(fruit) % 2 == 0:
            print(f"The length of {fruit} is even")
        elif len(fruit) % 2 != 0:
            print(f"The length of {fruit} is odd")
        else:
            print(f"The length of {fruit} is unkwon")
fruit_leng()



