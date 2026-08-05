class Employee:
    language="python"
    salary=1200000
    
    def __init__(self):
        print("i m creating an object")
    
    def getInfo(self):
        print(f"the language is {self.language}. The salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("good morning")
        
harry = Employee()
harry.name="harry"
print(harry.name,harry.salary)

rohan = Employee()                