vote=[(18,"Amit"),(17,"Sheela"),(16,"sunayana")]
for age,name in vote:
    if age > 16:
        print(f"eligible to manage {name}")
        break
else:
    print("not eligible to manage")