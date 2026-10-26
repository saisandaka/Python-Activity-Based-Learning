n= int(input("Enter number of subjects: "))
grace=0
passed=True
total=0
for i in range(n):
    marks=int(input("Enter marks: "))
    if marks>=35:
        total=total+marks
    elif marks>=33 and grace+(35-marks)<=2:
        grace=grace+(35-marks)
        total=total+35
    else:
        total=total+marks
        passed=False
print("Total Marks:", total)
print("Grace Marks Used:", grace)
if passed:
    print("Result: PASS")
else:
    print("Result: FAIL")
