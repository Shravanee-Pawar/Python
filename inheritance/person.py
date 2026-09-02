class Person:
    def details(self):
        print("Name: Rahul")
        print("Age: 20")

class Student(Person):
    def student_details(self):
        print("Roll No: 101")

s = Student()
s.details()
s.student_details()
