def rec(n):
    if n==0:
        print("All cups poured")
    while n>0:
        return rec(n-1)
rec(3)