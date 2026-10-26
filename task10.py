n=int(input("Enter number of students: "))
records=[]
for i in range(n):
    sid=input("Enter student ID: ")
    name=input("Enter student name: ")
    marks=int(input("Enter marks: "))
    attendance=int(input("Enter attendance: "))
    course=input("Enter course name: ")
    record=(sid, name, marks, attendance, course)
    records.append(record)
for i in range(n):
    sid, name, marks, attendance, course = records[i]
    print("Student:", name)
    if sid=="" or name=="" or course=="":
        print("Missing information")
    if marks<0 or marks>100:
        print("Invalid marks")
    if attendance<0 or attendance>100:
        print("Invalid attendance")
    for j in range(i):
        if records[j][0]==sid:
            print("Duplicate student ID")