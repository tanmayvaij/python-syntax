class A:
    def __init__(self):
        self.var1 = "class A var1"
        self.var2 = "class A var2"
class B(A):
    def __init__(self):
        super().__init__()
obj = B()
print(obj.var1)