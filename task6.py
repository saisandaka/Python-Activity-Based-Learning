n=int(input("Enter number of rows: "))
if n<=0:
    print("Invalid dimension")
else:
    for i in range(1,n+1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(1, i + 1):
            if j==1 or j==i:
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print()
    for i in range(n-1,0,-1):
        for j in range(n-i):
            print(" ", end="")
        for j in range(1,i+1):
            if j==1 or j==i:
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print()