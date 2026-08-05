class Employee:
    language = "Python"
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

harry = Employee()
harry.language = "JavaScript"

# Method 1
harry.getInfo()

# Method 2 (equivalent)
Employee.getInfo(harry)