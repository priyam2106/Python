class Employee:
     
     def __init__(self,salary,name, bond):
          self.salary =salary
          self.name=name
          self.bond=bond
    
    

     def get_salary(self):
        #   print(e)# self is reference of object in class that being to be created
          return self.salary
     
     def get_info(self):
          print(f" The name of the employee is {self.name} and salary is {self.salary}")


e1 = Employee(34000,"John Doe",4)

print(e1.get_salary())
e1.get_info()
     