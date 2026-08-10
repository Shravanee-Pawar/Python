class Employee:
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname, self.lname = value.split(" ")

e = Employee()

e.name = "Harry Pawar"

print(e.fname, e.lname)
print(e.name)