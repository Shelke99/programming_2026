class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(name,age)
    def update_age(self,new_age):
        self.age = new_age
Student1 = Student("Rahul", 20)
Student2 = Student("Priyanka",25)
print(Student1.name)
