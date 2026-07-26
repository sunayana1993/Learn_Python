#Take snack input from user
#If it is samosa or cookies take the order
#If not order is unavailable
snack=input("Entered your preferred snack").lower()
print(f"snack is: {snack}")

if snack=="samosa" or snack=="cookie":
    print(f"Great order! We will serve you {snack}")
else:
    print(f"Sorry! We only serve cookie or samosa with chai")