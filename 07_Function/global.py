chai_type="ginger"

def print_order():
   chai_type="lemon"
   def print_chai():
      #global chai_type
      chai_type="mint"
      print(f"chai type is {chai_type}")
   print_chai()
print_order()
print(f"chai type is {chai_type}")
