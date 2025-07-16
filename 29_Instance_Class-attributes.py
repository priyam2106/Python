class Employee:
     company="Asus"
     
     def __init__(self,salary,name, bond ,company):
          self.salary =salary
          self.name=name
          self.bond=bond
          self.company=company
    
    

     def get_salary(self):
        #   print(e)# self is reference of object in class that being to be created
          return self.salary
     
     def get_info(self):
          print(f" The name of the employee is {self.name} and salary is {self.salary}")


e1 = Employee(3400,"john",3,"Rays It")
print(e1.company)
print(Employee.company)

print(dir(e1))