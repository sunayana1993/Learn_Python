def chai_customer():
    print("Welcome!What chai would you like?")
    #you want to send data to yield
    order=yield
    while True:
        print(f"Preparing : {order}")
        order=yield

stall=chai_customer()
next(stall)
stall.send("masala chai")
stall.send("ginger chai")

