def rem(l, word):
    n = []
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
         
l = ["harry","rohan","shubham","an"] 
print(rem(l,"an"))   
    