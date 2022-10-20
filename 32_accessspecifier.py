class Employee:
    var = 34
    _myprotec = 5
    __protected = 45
obj = Employee()
print(obj.var)
print(obj._myprotec)
print(obj._Employee__protected)