#In dictionary order doesn't matter
#It has key:value format
dict_label=dict(chai="kadak",type="milk based",sugar=2)
print(f"chai type is {dict_label}")

chai_recipe={}
chai_recipe["base"]="black tea"
chai_recipe["liquid"]="milk"

print(f"chai recipe is {chai_recipe}")
print(f"chai recipe base is {chai_recipe["base"]}")
print(f"chai recipe bas:{chai_recipe["liquid"]}")
print(f"chai receipe : {chai_recipe}")
del chai_recipe["liquid"]
print(f"chai recipe now: {chai_recipe}")

chai_order=dict(type="Masala Chai",size="Large",level=2)
print(f"chai order is {chai_order}")
print(f"sugar in chai_order {'sugar' in chai_order}") #membership
print(f"level in chai_order {'level' in chai_order}")

#print(f"order details(keys): {chai_order.keys()}")
#print(f"Order details(values): {chai_order.values()}")

#print(f"Order details(items): {chai_order.items()}")

last_item=chai_order.popitem()
print(f"last item is {last_item}")

extra_spice={"cardamom":"crushed","ginger":"sliced"}
chai_recipe.update(extra_spice)
#updated chai recipe
print(f"updated chai recipe is {chai_recipe}")