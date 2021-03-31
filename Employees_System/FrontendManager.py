import empoyee_manager
class FrontendManager:
    def __init__(self):
        self.employees_manger = empoyee_manager.Employee_Manager()

    def print_menu(self):
        print('\nProgram Options:')
        messages = [
            '1) Add a new employee',
            '2) List all employees',
            '3) Delete by age range',
            '4) Update salary given a name',
            '5) End the program'
        ]
        print('\n'.join(messages))
        msg = input('Enter your choice (from 1 to {len(messages)}): ')
        return int(msg)

    def run(self):
        while True:
            choice = self.print_menu()
            if choice==1:
                self.employees_manger.add_employee()
            elif choice==2:
                self.employees_manger.print_employee()
            elif choice==3:
                self.employees_manger.delete()
            elif choice==4:
                self.employees_manger.update_salary()
            else:
                break

        
    

if __name__=="__main__":
    f=FrontendManager()
    f.run()
