from employee import Employee


class Backend:
    def __init__(self) -> None:
        self.employees= []
    
    def add_employee(self):
        print('\n enter employee data: ')
        name= input('enter the name: ')
        age= int(input('enter the age: '))
        salary= int(input('enter the salary: '))
        self.employees.append(Employee(name,age,salary))

    def list_employees(self):
        if not self.employees:
            print('no employee found ')
            return
        print('\n*** employee list ***')
        for employee in self.employees:
            print(employee)

    def delete_employee(self, age_from, age_to):
        if age_from>age_to:
            age_from,age_to=age_to,age_from
        for i in range(len(self.employees)-1,-1,-1):
            if age_to >= self.employees[i].age >=age_from:
                self.employees.pop(i)
    
    def find_emplyee_by_name(self,name):
        for emp in self.employees:
            if emp.name== name:
                return emp
        return None
    
    def update_salary(self,name,salary):
        emp = self.find_emplyee_by_name(name)
        if not emp:
            print('not found')
        else:
            emp.salary= salary