class Student:
    def get_student(self):
        self.name = input("Enter name: ")
        self.roll = int(input("Enter roll number: "))

class Marks(Student):
    def get_marks(self):
        self.m1 = int(input("Enter marks of subject 1: "))
        self.m2 = int(input("Enter marks of subject 2: "))
        self.m3 = int(input("Enter marks of subject 3: "))

    def display(self):
        total = self.m1 + self.m2 + self.m3
        percentage = total / 3

        print("Name:", self.name)
        print("Roll No:", self.roll)
        print("Total:", total)
        print("Percentage:", percentage)

obj = Marks()
obj.get_student()
obj.get_marks()
obj.display()
