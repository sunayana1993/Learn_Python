menu=["chai","coffee","sandwich","bread"]
print(list(enumerate(menu)))

for idx,item in enumerate(menu,start=1):
    print(f"{idx}:{item}")