w = int(input("Enter your weight: "))
unit = input("K (KG) or L (lbs): ")

if unit.upper() == "L":
    print(f"Your weight : {w*0.45} KG")

else :
    print(f"Your weight : {w//0.45} lbs")