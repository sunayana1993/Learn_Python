menu=["tea","Out of stock","ginger","discontinued","tulsi"]

for flavour in menu:
    if flavour=="Out of stock":
        continue
    if flavour=="discontinued":
        break
    print(f"flavour is {flavour}")

print("out of loop")