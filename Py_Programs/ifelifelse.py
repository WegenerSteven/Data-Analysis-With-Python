discount = 0
amount = int(input("Enter Amount :"))
if amount > 1000:
    discount = amount * 0.10
elif amount > 500:
    discount = amount * 0.05
else:
    discount = 0
print('Discount =',discount)
print('Net Amount',amount - discount)

# #single statements suites
# marks = int(input("Enter Marks:"))
# if marks >= 50:print('Pass')
# else:print("Fail")
