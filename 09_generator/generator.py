def serve_chai():
    yield "cup1:Masala chai"
    yield "cup2:ginger chai"
    yield "cup3:elaichi chai"

stall=serve_chai()
for tea in stall:
    print(tea)