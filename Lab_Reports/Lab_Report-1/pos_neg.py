numbers = [10, -5, 0, 7, -22, 0, 15, -3, 0]
pos = 0
neg = 0
zero = 0

for num in numbers:
    if num > 0:
        pos = pos+1
    elif num < 0:
        neg = neg+1
    else:
        zero = zero+ 1
print("Total Positive numbers:", pos)
print("Total Negative numbers: ", neg)
print("Total Zeros: ",zero)