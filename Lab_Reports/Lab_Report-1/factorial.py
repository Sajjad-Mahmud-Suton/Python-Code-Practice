fact=1
num = int(input("Enter your number: "))
for i in range(1,num+1):
    fact = fact*i
    
print (f"Factorial of {num} is: ",fact)