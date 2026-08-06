#Code duplication
#explicit call
#super()
class chai:
    def __init__(self,type_,strength):
        self.type_=type_
        self.strength=strength
       
#code dulication
class GingerChai(chai):
    def __init__(self,type_,strength,spice_level):
         self.type_=type_
         self.strength=strength
         self.spice_level=spice_level

#explicit calling
class GingerChai(chai):
    def __init__(self,type_,strength,spice_level):
        chai.__init__(self,type_,strength)
        self.spice_level=spice_level

class GingerChai(chai):
    def __init__(self,type_,strength,spice_level):
        super().__init__(type_,strength)
        self.spice_level=spice_level
        


    


    
