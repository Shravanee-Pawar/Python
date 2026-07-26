marks ={
    "harry" : 100,
    "shubham" : 566,
    "rohan": 23
}
print(marks.items())
print (marks.values())
print(marks.keys())
marks.update({"harry":99 , "renuka":100})
print(marks)
print(marks.get("harry")) #prints error
print(marks["harry"]) #returns error