arr = [10, 21, 4, 45, 66, 93, 11]
small=arr[0]
for i in arr:
    if i<= small:
        small = i

print("Smallest number is : ",small)
    