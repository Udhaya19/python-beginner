class Student:
    college_name = "Agni College"

    def student_details(self):
        print("Hi,Hello")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Details")
        Student.college_name
        print("User_details",name,age)

s = Student()
s.student_details('udhaya,20')

