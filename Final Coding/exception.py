try:
    age = int(input("Age : "))
  
    income = 20000
    risk = income/age
    print(f"Risk is : {risk}")
   
    
    print(f"Your Age is: {age}")
except ValueError:
    print("Invalid Value.")
except ZeroDivisionError:
    print("Your inserted 0. Which is invalid value")