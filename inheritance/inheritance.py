class employee:
    company = "Google"
    def show(self):
        print(f"the company name is {self.company}")
class programmer(employee):
    company = "Youtube"
    def show(self):
        print(f"the company name is {self.company}")    
a = employee()
b= programmer()
print(a.company , b.company)          