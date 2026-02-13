print("Printing 1 to 5:")
i=1
while i <= 5:
    print(i)
    i += 1

print("\nPrinting 1 to 5 using while loop with continue:")
i = 1
while i <= 5:
    i= i + 1
    if i == 3:
        continue
    print(i)
print("\nPrinting 1 to 5 using while loop with break:")
i= 1
while i <= 5:
    i = i + 1
    if i == 3:
        break
    print(i)