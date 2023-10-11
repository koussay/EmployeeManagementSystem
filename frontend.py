from backend import Backend
from helper import input_valid


class Frontend:
    def __init__(self) -> None:
        self.backend= Backend()

    def print_startmenu(self):
        print('\nprogram options: ')
        print("1- add new employee")
        print("2- list all employees")
        print("3- delete employee by age range")
        print("4- update salary given a name")
        print("5- end the program")

        msg= f'enter your choice from 1 to 5 '
        return input_valid(msg,1, 5)
    
    def run(self):
        while True:
            choice= self.print_startmenu()
            if choice==1:
                self.backend.add_employee()
            elif choice==2:
                self.backend.list_employees()
            elif choice==3:
                age_from= input_valid('enter age from')
                age_to= input_valid('enter age to')
                self.backend.delete_employee(age_from,age_to)
            elif choice==4:
                name= input('enter the employee name ')
                salary= input_valid('enter new salary')
                self.backend.update_salary(name, salary)
            else:
                break