arr = [10, 21, 4, 45, 66, 93, 11]
odd=0
even = 0
for i in arr:
    if i % 2 == 0:
        even = even + i
    
    else:
        odd = odd + i
 
print("Sum of even numbers: ",even)
print("Sum of odd numbers: ",odd)