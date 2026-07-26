#Tuples comes with ()
#Tuples are immutable
masala_spices=("cardamom","ginger","cinnamon")
(spice1,spice2,spice3)=masala_spices
print(f"spices are {spice1},{spice2},{spice3}")

cardamom,ginger=2,1
print(cardamom,ginger)
cardamom,ginger=ginger,cardamom
print(cardamom,ginger)
#python remembers the ratio, variable swapping
