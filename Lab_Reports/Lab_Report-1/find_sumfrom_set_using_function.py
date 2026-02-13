def summation(*num):
    sum=0
    for i in num:
        sum = sum+i
    return sum

res1 = summation(10, 20, 30)
res2 = summation(5, 15, 25, 40, 50, 60)
print("Sum of set : ",res1)
print("Sum of set : ",res2)
