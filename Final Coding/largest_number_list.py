num = [3,6,2,6,8,3,4]
max = num[0]
for i in num[1:]:
    if i>=max:
        max = i
print(max)