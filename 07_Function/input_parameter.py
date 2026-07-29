chai_type="Ginger"
def prepare_chai(chai_type):
    print("Preparing ",chai_type)

prepare_chai(chai_type)
print(chai_type)

chai=[1,2,3]

def edit_chai(cup):
    chai[1]=42

edit_chai(chai)
print(chai)

def special_chai(*ingredients,**masala):
    print("Ingredients are :",ingredients)
    print("Masala are :",masala)

special_chai("milk","water",masala1="ginger",masala2="lemon")


def addorder(order=[]):
    order.append("Masala")
    print(order)
addorder()

def addorder1(order=None):
    print(order)

addorder1()