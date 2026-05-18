price = 1000000
good_credit = True

if good_credit:
    payable = 0.1*price
else:
    payable = 0.2*price

print(round(payable))
print(f"With Commision: {round(payable)}")