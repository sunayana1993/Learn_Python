#List datastructure are mutable
#List is called as array in another language
#ingredients to make chai
ingredients=["milk","tea leaf","water","sugar"]
ingredients.append("jaggery")
print(f"chai making ingredients are {ingredients}")
ingredients.remove("jaggery")
print(f"chai making ingredients are {ingredients}")

chai_ingredients=["milk","water"]
spice_mix=["ginger","cardamom"]
chai_ingredients.extend(spice_mix)
print(chai_ingredients)

last_added=chai_ingredients.pop()
print(f"last added {last_added}")
chai_ingredients.reverse()
print(f"reverse={chai_ingredients}")

sugar_level=[1,2,3,4]
print(f"sugar level max: {max(sugar_level)}")
print(f"sugar level min: {min(sugar_level)}")

base_liquid=["water","milk"]*3
print(f"output: {base_liquid}")

raw_spice_data=bytearray(b"CINNAMON")
print(f"raw_spice_data: {raw_spice_data}")
raw_spice_data=raw_spice_data.replace(b"CINN",b"CARD")
print(f"raw_spice_data: {raw_spice_data}")
