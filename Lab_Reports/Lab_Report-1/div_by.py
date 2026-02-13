sum = 0
for i in range(50,101):
    if i%3 == 0 and i%5 != 0:
     sum = sum+i
print("Sum is : ",sum)