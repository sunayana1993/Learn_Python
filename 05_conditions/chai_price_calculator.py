cup_size=input("Enter size of cup large/medium/small :").lower()

if cup_size=="small":
    print(" Chai price is Rs.10")
elif cup_size=="medium":
    print("Chai price is Rs.15")
elif cup_size=="large":
    print("Chai price is Rs.20")
else:
    print("unknown cup size")