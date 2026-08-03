line = 1 
with open ("log.txt") as f:
    line = f.readline()
    
if("Python" in line):
    print("yes python is present")
else:  
    print("no python")      