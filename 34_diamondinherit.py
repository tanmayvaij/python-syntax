class A:
    def met(self):
        print("A")
class B(A):
    def met(self):
        print("B")
class C(A):
    def met(self):
        print("C")
class D(B, C):
    def met(self):
        print("D")
a = A()
b = B()
c = C()
d = D()
d.met()