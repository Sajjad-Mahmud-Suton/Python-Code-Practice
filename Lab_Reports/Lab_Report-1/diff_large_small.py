arr = [10, 21, 4, 45, 66, 93, 11]
large=arr[0]
for i in arr:
    if i >= large:
        large = i

print("Large number is : ",large)
small=arr[0]
for i in arr:
    if i<= small:
        small = i

print("Smallest number is : ",small)

print("Difference between largest & smallest: ",large-small)


    

