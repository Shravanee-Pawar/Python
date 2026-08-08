class employee:
    company = "Google"

    def show(self):
        print(f"The company name is {self.company}")


class coder:
    language = "Python"

    def printLanguage(self):
        print(f"The language is {self.language}")


class programmer(employee, coder):
    company = "Youtube"

    def show(self):
        print(f"The company name is {self.company}")


a = employee()
b = programmer()

b.show()
b.printLanguage()