class Employee:
    no_of_leaves = 5
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def printdetails(self):
        print(f"{self.name} {self.age} {self.salary}")
    @classmethod
    def changeleaves(cls, leaves):
        cls.no_of_leaves = leaves
    @staticmethod
    def printsom(val):
        print("This is a " + val)
emp1 = Employee("Tanmay", 27, 56000)
emp1.printdetails()
print(emp1.no_of_leaves)
emp1.changeleaves(45)
print(emp1.no_of_leaves)
Employee.printsom("Statement")