word = "information"
with open("myfile.txt" "r") as f:
    content = f.read()
    
contentnew=content.replace("information","sunny")
with open("myfile.txt" "w") as f:
    f.write(contentnew)   