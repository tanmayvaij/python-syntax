class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def printdetails(self):
        print(f"{self.name} {self.age} {self.salary}")
class Programmer:
     def __init__(self, name, language):
         self.name = name
         self.language = language
class CoolGuy(Employee, Programmer):
    pass
a = CoolGuy("Tanmay", 16, None)
a.printdetails()