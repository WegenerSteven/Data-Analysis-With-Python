discount = 0
amount = int(input("Enter Amount"))
if amount > 1000:
    discount = amount*0.10
print("Discount =", discount)
print('Net amount', amount-discount)