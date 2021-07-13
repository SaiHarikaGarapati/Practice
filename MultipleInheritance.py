#Multiple Inheritance
class Employee():  #Parent class
    def __init__(self):
        self.Name = input("Name_")
        self.Age =  input("Age_")
class Work():     #Parent class
    def __init__(self):
        self.work = input("Work_")
class Salary():    #Parent class
    def __init__(self):
        self.salary = input("Salary_")
class EmployeeData(Employee,Work,Salary):    #Child class
    def __init__(self):
        Employee.__init__(self)
        Work.__init__(self)
        Salary.__init__(self)
    def dataOnTerminal(self):
        print(self.Name)
        print(self.Age)
        print(self.work)
        print(self.salary)
obj = EmployeeData()
obj.dataOnTerminal()