numbers = [12, 45, 2, 41, 31, 10, 8, 45]

largest = 0
sec_larg = 0

for num in numbers:
    if num > largest:
        sec_larg = largest
        largest = num
    elif num > sec_larg and num != largest:
        sec_larg = num

print(f"The second largest is: ",sec_larg)