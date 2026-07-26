friends = [ "apple" , "orange" , 5 ,345.06]
print (friends[0]) #lists are mutable
friends[0]= "grapes"
print(friends[0])
print (friends[1:4])
l1 = [1 , 34 , 62 , 2 , 6 ,11]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.insert(3 , 33333)
print(l1)
l1.pop(3)
print(l1)
l1.remove(2)
print(l1)