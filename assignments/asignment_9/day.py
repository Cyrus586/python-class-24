from datetime import datetime

# EXAMPLE 1
# using user input to write their own daytime for the schedule
def input_day():
    print("EXAMPLE 1")
    my_day = int(input("Enter the current day of the week (1-7): "))
    
    if my_day == 1:
        print("Monday: Organizing for the week ahead")
    elif my_day == 2:
        print("Tuesday: Planing my time table to code for the week")
    elif my_day == 3:
        print("Wednesday: Taking my clothes to the washing machine")
    elif my_day == 4:
        print("Thursday: Playing games on my PS4 consle and coming to the institute")
    elif my_day == 5:
        print("Friday: Going for Juma prayers")
    elif my_day == 6:
        print("Saturday: Doing my weekly assignment left by the teacher")
    elif my_day == 7:
        print("Sunday: Thats my day off so i chill")
    else:
        print("Invalid input, please pick from 1-7")
input_day()


print("=====================================")
print("EXAMPLE 2")




# EXAMPLE 2
# using the import method `datetime` which tells us the current day 

def current_daytime():
    current_day = datetime.now().weekday() + 1
    if current_day == 1:
        return "Monday: Planing and Organizing for the week ahead"
    elif current_day == 2:
        return "Tuesday: Team meeting and collaboration"
    elif current_day == 3:
        return "Wednesday: Mid-week assessments and assignments from  the teacher"
    elif current_day == 4:
        return "Thursday: Playing games on my PS4 consle and coming to the institute"
    elif current_day == 5:
        return "Friday: Going for Juma prayers"
    elif current_day == 6:
        return "Saturday: Doing my weekly assignment left by the teacher"
    elif current_day == 7:
        return "Sunday: Thats my day off so i chill"
    else:
        return "Day Not found "
    
    
print(current_daytime())