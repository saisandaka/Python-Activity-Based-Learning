students=int(input("Enter number of students: "))
subjects=int(input("Enter number of subjects: "))
marks=[]
for i in range(students):
    row=[]
    print("Enter marks for student",i+1)
    for j in range(subjects):
        m=int(input("Enter marks: "))
        row.append(m)
    marks.append(row)
for i in range(students):
    total=sum(marks[i])
    average=total/subjects
    print("Student", i+1, "Total:", total, "Average:", average)
for j in range(subjects):
    total=0
    for i in range(students):
        total=total+marks[i][j]
    average=total/students
    print("Subject", j+1, "Average:", average)
    if average<35:
        print("Warning: Low subject average")