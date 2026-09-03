smallest = None

for i in range(5):
    n = int(input("Enter number: "))

    if smallest is None or n < smallest:
        smallest = n

print("Smallest =", smallest)
