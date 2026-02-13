num = int (input("Enter your number: "))

if(num>1):
    for i in range(2,num):
        if num%i ==0:
            print("Not a prime number")
            break
    else:
            print("Prime Number.")
  
else:
    print("Not a prime number")