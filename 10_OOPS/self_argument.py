#self is a reference passed in method inside class which is reference to all the parameters
class chai:
    size=150

    def describe(self):
        return f"A {self.size} chai cup here"

cup=chai()
print(cup.describe()) #reference of cup is passed
print(chai.describe(cup))#doesn't know which reference I am passing

cup_two=chai()
cup_two.size=300
print(chai.describe(cup_two))