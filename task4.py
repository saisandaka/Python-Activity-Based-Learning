n=int(input("Enter number of students: "))
for i in range(n):
    name=input("Enter student name: ")
    marks1=int(input("Enter first exam marks: "))
    marks2=int(input("Enter second exam marks: "))
    marks3=int(input("Enter third exam marks: "))
    total=marks1+marks2+marks3
    average=total/3
    print("\nStudent Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", average)
    if marks3>marks1:
        print("Performance: Improved")
    elif marks3<marks1:
        print("Performance: Declined")
    else:
        print("Performance: No Change")
    if marks1<35 or marks2<35 or marks3<35:
        print("Warning: Weak performance in at least one exam")
