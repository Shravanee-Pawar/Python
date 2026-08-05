class Employee:
    language = "Python"   # Class variable

    def __init__(self, name, salary):
        self.name = name          # Instance variable
        self.salary = salary      # Instance variable
        print("I am creating an object")

    def getInfo(self):
        print(f"Name: {self.name}")
        print(f"Language: {self.language}")
        print(f"Salary: {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

# Creating objects
harry = Employee("Harry", 120000)
rohan = Employee("Rohan", 150000)

# Accessing instance variables
print(harry.name, harry.salary)
print(rohan.name, rohan.salary)

# Calling methods
harry.getInfo()
rohan.getInfo()
Employee.greet()