secret = 5
i = 1
while i<=3:
    num = int(input("Guess: "))
    i = i+1
    if num==secret:
        print("Congrats!!!!! You won")
        break
else:
    print("Better luck next time")