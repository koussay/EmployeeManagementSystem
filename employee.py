class Employee:
    def __init__(self,name,age,salary) -> None:
        self.name= name
        self.age= age
        self.salary= salary
    
    def __str__(self) -> str:
        return f'employee: {self.name}, age {self.age}, salary {self.salary}'