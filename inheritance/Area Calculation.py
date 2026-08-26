class Shape:
    def display(self):
        print("Area Calculation")

class Circle(Shape):
    def area(self):
        r = float(input("Enter radius: "))
        print("Area of Circle:", 3.14 * r * r)

class Rectangle(Shape):
    def area(self):
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        print("Area of Rectangle:", l * b)

c = Circle()
c.display()
c.area()

r = Rectangle()
r.display()
r.area()
