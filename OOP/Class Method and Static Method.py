class Demo:
    count = 0

    def __init__(self):
        Demo.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def greet():
        return "Hello"

Demo()
Demo()
print(Demo.get_count())
print(Demo.greet())
