class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def printdetails(self):
        print(f"{self.name} {self.age} {self.salary}")
class Programmer(Employee):
    pass
prog1 = Programmer("Tanmay", 18, None)
prog1.printdetails()