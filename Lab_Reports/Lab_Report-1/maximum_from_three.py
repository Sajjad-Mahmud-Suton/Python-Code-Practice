def max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = 25
num2 = 78
num3 = 42

result = max(num1, num2, num3)
print("The maximum number is: ",result )