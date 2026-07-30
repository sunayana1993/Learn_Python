#set={expression for item in set if condition}
menu=["Iced chai","Iced chai","Ginger chai","Kesar Chai"]

set_comp={tea for tea in menu}
print(set_comp)

menu_dict={
    "Ginger chai":["ginger","milk","water"],
    "Elaichi chai":["Elaichi","milk","water"]
}

set_chai={spice for ingredient in menu_dict.values() for spice in ingredient }
print(set_chai)