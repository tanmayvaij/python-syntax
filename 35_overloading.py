class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return f"{real} + ({imag})i"
    def __repr__(self):
        return f"{self.real} + ({self.imag})i"
obj1 = complex(4, 5)
obj2 = complex(5, 4)
print(obj1 + obj2)
print(obj1)