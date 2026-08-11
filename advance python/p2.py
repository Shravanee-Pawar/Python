a = int(input("enter a number"))
b = int(input("enter second number"))
if(b == 0):
    raise ZeroDivisioonError("hey")
else:
    print(f"the division a/b is {a/b}")