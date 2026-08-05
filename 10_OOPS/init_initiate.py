#init is to create an object->initiate
class chaiOrder:
    #initiate object
    def __init__(self,type_,size):
        self.type=type_
        self.size=size

    def summary(self):
        return f"chai of type {self.type} and size {self.size}"

order=chaiOrder("Masala", 50)
print(order.summary())