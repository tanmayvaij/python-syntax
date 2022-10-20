class Grandfather:
    def def1(self):
        print("grandfather")
class Father(Grandfather):
    def def2(self):
        print("father")
class Son(Father):
    def def3(self):
        print("son")
obj = Son()
obj.def1()
obj.def2()
obj.def3()