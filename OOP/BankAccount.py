class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display(self):
        print("Balance:", self.balance)


account = BankAccount(5000)

account.deposit(2000)
account.withdraw(1000)

account.display()
