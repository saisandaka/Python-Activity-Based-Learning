
n = int(input("Enter number of products: "))
total = 0
for i in range(n):
    name=input("Enter product name: ")
    price=int(input("Enter price: "))
    quantity=int(input("Enter quantity: "))
    amount=price*quantity
    total=total+amount
    print("Product:", name)
    print("Actual Amount: Rs.", amount)
if total>=2000:
    discount=total*(10/100)
else:
    discount=0
final_amount=total-discount
print("Total Amount: Rs.", total)
print("Discount: Rs.", discount)
print("Final Bill: Rs.", final_amount)
