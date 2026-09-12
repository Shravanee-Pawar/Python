class Number:
    def __init__(self, n):
        self.n = n

    def check(self):
        if self.n % 2 == 0:
            print("Even")
        else:
            print("Odd")


obj = Number(7)
obj.check()
