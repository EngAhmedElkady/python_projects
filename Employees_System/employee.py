class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.salary=salary
        self.age=age
    def get_age(self):
        return self.age
    def get_salary(self):
        return self.salary
    def get_name(self):
        return name
    def update_salary(self,newsalary):
        self.salary=newsalary

