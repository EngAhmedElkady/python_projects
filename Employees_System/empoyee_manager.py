import employee
class Employee_Manager:
    Lst=[]
    def add_employee(self):
        name=input("Enter name : ")
        age=input("Enter age : ")
        salary=input("Enter salary : ")
        
        Employee_Manager.Lst.append(employee.Employee(name,age,salary))
    def print_employee(self):
        for emp in self.Lst:
            print(f"Employee: {emp.name}  age: {emp.age} salary: {emp.salary}")
    
    def update_salary(self):
        find=False
        name_=input("Enter name : ")
        new_salary=input("Enter new salary : ")
        for emp in self.Lst:
            if emp.name==name_:
                emp.salary=new_salary
                print("done")
                find=True
                break
        if not find:
            print("Error:name not found")

    def delete(self):
        f_age=int(input("Enter age from:"))
        t_age=int(input("Enter age to  :"))
        for i in range(len(self.Lst)-1,-1,-1):
            emp=self.Lst[i]
            if f_age<=int(emp.age)<=t_age:
                self.Lst.remove(emp)
        

if __name__=="__main__":
    emp1=employee.Employee("Ahmed","20","6000")
    emp2=employee.Employee("Ali","30","6000")
    emp3=employee.Employee("mostafl","25","6000")
    emp4=employee.Employee("el","40","6000")
    emp_manager=Employee_Manager()
    emp_manager.add_employee(emp1)
    emp_manager.add_employee(emp2)
    emp_manager.add_employee(emp3)
    emp_manager.add_employee(emp4)
    emp_manager.print_employee()
    emp_manager.delete()
    emp_manager.print_employee()


