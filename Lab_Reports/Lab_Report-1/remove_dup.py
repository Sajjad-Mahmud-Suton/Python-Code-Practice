arr = [10, 20, 10, 30, 40, 20, 50, 10]
arr1 = []

for item in arr:
    if item not in arr1:
        arr1.append(item)

print("Original List:", arr)
print("Without Duplicates:", arr1)