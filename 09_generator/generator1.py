def func():
    return ["cup1","cup2","cup3"]

print(func())

def func_gen():
    yield "cup1"
    yield "cup2"
    yield "cup3"

print(func_gen()) #will give memory reference

# to get the value you use next
print(next(func_gen()))