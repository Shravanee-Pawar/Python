with open ("log.txt") as f:
    content = f.read()
    
if("Python" in content):
    print("yes python is present")
else:  
    print("no python")      