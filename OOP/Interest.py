class Interest:
    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t

    def calculate(self):
        return (self.p * self.r * self.t) / 100


obj = Interest(10000, 5, 2)
print("Simple Interest:", obj.calculate())
