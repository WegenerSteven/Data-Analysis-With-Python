discount = 0
amount = int(input("Enter Amount"))
if amount > 1000:
    discount = amount * 0.10
else: 
    discount = amount * 0.05
print('Discount= ',discount)
print('Net Amount', amount - discount)