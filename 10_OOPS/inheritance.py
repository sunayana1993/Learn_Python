#constructor variable need not to get created again
class BaseChai:
    def __init__(self,type_):
        self.type=type_

    def prepare(self):
        return f"print chai {self.type}"

#inherritance
class MasalaChai(BaseChai):
    def add_spices(self):
        print("adding cardamom,ginger,spices")

#composition
class chaiShop:
    chai_cls=BaseChai

    def __init__(self):
        self.chai=self.chai_cls("Regular")

    def prepare(self):
        print(f"serving {self.chai.type} ")
        self.chai.prepare()

class FancyChaiShop(chaiShop):
    chai_cls=MasalaChai

shop=chaiShop
fancy=FancyChaiShop
print(shop.prepare())