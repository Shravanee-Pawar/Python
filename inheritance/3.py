class Employee:
    salary = 234
    _increment = 20

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, salary):
        self._increment = ((salary / self.salary) - 1) * 100

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment / 100)


e = Employee()

print(e.salaryAfterIncrement)