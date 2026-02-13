marks = int(input("Enter your marks: "))
if marks>=80:
    print("A+")

elif 80>marks>70:
    print("A")

elif 70>marks>60:
    print("A-")
    
elif 60>marks>50:
    print("B")
    
elif 50>marks>40:
    print("C")

elif 40>marks>32:
    print("D")

else:
    print("F")