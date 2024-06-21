class Employees:
    def __init__(self,name,employee_id,salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

class managers(Employees):
    def __init__(self,name,employee_id,salary,department,list_of_employees):
        super().__init__(name,employee_id,salary)
        self.department = department
        self.list_of_employees = list_of_employees
    def display_employee(self):
        print("This is the list of employees i manage", self.list_of_employees)
class developers(Employees):
    def __init__(self,name,employee_id,salary,programming_languages):
        super().__init__(name,employee_id,salary)
        self.programming_languages = programming_languages
    def add_skill(self):
        print("These are my programming languages", self.programming_languages())
class interns(Employees):
    def __init__(self,name,employee_id,salary,school_name,graduation_year):
        super().__init__(name,employee_id,salary)
        self.school_name = school_name
        self.graduation_year = graduation_year
    def display_interns(self):
        print(f"I studied at {self.school_name} and graduated the year {self.graduation_year}")

Employees= managers('Ferran','123123',123420,'Interns','Sass,Ferts,Chris')
managers.display_employee()


