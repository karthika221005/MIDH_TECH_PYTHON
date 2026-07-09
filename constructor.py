class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self, number):
        print(f"Student{number} Name: {self.name}, Age: {self.age}")

s1 = Student("Karthika", 22)
s2 = Student("Kavya", 20)
s3 = Student("Sathvika", 21)
s4 = Student("Divya", 23)

s1.display(1)
s2.display(2)
s3.display(3)
s4.display(4)
