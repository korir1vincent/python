class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name= first_name
        self.last_name= last_name
        self.age= age
    def print_name(self):
        print(f"My name is {self.first_name} {self.last_name} and i am {self.age} years old")
class Student(Person):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
myStudent = Student('Gregory','Isaacs','54')
myStudent.print_name()
myStudent2 = Student('Vincent','Kiplangat','24')
myStudent2.print_name()
myStudent3 = Student('Dave','Kipkorir','34')
myStudent3.print_name()
myStudent4 = Student('Sause','Seas','32')
myStudent4.print_name()