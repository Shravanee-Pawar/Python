f = open("poem.txt")
c = f.read()
if("twinkle" in c):
    print("word present")
else:
    print("word absent")
f.close()        
