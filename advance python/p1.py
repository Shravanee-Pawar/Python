try:
    a = int(input("hey,enter a number:"))
    print(a)
except ValueError as v:
    print("heyyy")
    print(v)        
except exception as e:
    print(e)    
print("thank you")    