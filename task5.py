subject1=input("Enter first subject: ")
day1=input("Enter first day: ")
period1=int(input("Enter first period: "))
room1=input("Enter first room: ")
subject2=input("Enter second subject: ")
day2=input("Enter second day: ")
period2=int(input("Enter second period: "))
room2=input("Enter second room: ")
class1=(day1, period1, room1)
class2=(day2, period2, room2)
if class1 == class2:
    print("Timetable Conflict Detected")
else:
    print("No Timetable Conflict")