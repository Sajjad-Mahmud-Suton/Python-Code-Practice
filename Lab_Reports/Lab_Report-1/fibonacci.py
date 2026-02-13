num = int(input("Enter your number: "))
n1 = 0
n2 = 1
temp=0
count = 0
if num== 1:
    print(n1)
else:
    print("Fibonacci series:")
    while count < num:
        print(n1)
        temp = n1 + n2
        n1 = n2
        n2 = temp
        count = count+1