arr = [10, 21, 4, 45, 66, 93, 11]
large=arr[0]
for i in arr:
    if i >= large:
        large = i

print("largest number is : ",large)
    