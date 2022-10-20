class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def printdetails(self):
        print(f"{self.name} {self.age} {self.salary}")
emp1 = Employee("Tanmay", 27, 56000)
emp1.printdetails()