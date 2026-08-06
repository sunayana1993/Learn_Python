class A:
    label="label A:returning from A"

class B(A):
    label="label B:returning from B"

class C(B):
    label="label C:returning from C"

class D(B,A):
    pass

cup=D()
print(cup.label)
print(D.__mro__)
