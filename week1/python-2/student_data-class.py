class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def get_info(self):
        return f"Name:{self.name}, Age:{self.age}, Marks:{self.marks}/50"
    
    def update_marks(self):
        self.marks+=2

a=Student(name="Alice",age=20,marks=45)
b=Student(name="Bob",age=22,marks=48)

# print(a.get_info())
# print(b.get_info())

a.update_marks()
print(a.get_info())
b.update_marks()
print(b.get_info())