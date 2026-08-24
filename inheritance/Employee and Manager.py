class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print(self.name)
        print(self.salary)
        print(self.department)


m = Manager("Rahul", 50000, "IT")
m.display()
