n=int(input("Enter number of transactions: "))
transactions=[]
for i in range(n):
    tid=input("Enter transaction ID: ")
    amount=int(input("Enter transaction amount: "))
    ttype=input("Enter type (deposit/withdrawal): ")
    transaction=(tid, amount, ttype)
    transactions.append(transaction)
for i in range(n):
    tid, amount, ttype = transactions[i]
    print("Transaction:", tid, "Amount:", amount, "Type:", ttype)
    if amount<=0:
        print("Invalid transaction amount")
    if ttype!="deposit" and ttype!="withdrawal":
        print("Invalid transaction type")
    for j in range(i):
        if transactions[j][0]==tid:
            print("Duplicate transaction ID")