class Employee:
    company="Hp"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    # Instance Method (default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)
    # Static Method 
    @staticmethod
    def sum(a,b):
        return a+b
    
    # Class Method
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company   



e1=Employee("Jack",3455)
e2=Employee("Jill",3455)
print(Employee.company)
e1.print_info()

print(e2.sum(53,4))
e1.print_company()
e1.change_company("Asus")
e1.print_company()

  

        