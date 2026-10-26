n=int(input("Enter number of students: "))
for i in range(n):
    name=input("Enter student name: ")
    marks=int(input("Enter marks: "))
    attendance=int(input("Enter attendance: "))
    income=int(input("Enter family annual income: "))
    if marks>=80 and attendance>=75 and income<=200000:
        print(name, "is eligible for scholarship")
    else:
        print(name, "is not eligible for scholarship")