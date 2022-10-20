# Python Syntax

### 1. Hello World
```python
print("Hello World")

print("1 first statement", end=" ")
print("1 second statement")

print("2 first statement", "2 second statement")

print("tan \nis good\t hi")
print("\"")
```
<br/>

### 2. Comments
```python
# This is a single line comment

""" This is a 
multiline comment """
```
<br/>

### 3. Data Types
```python
a = 1
b = 6.7
c = "word"
d = True
e = None

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

var1 = 14
var2 = 76
var3 = "45"
var4 = "105"
print(var1 + var2)
print(var3 + var4)
print(str(14) + str(76))
print(10 * var3)

"""
Output:- 

1 <class 'int'>
6.7 <class 'float'>
word <class 'str'>
True <class 'bool'>
None <class 'NoneType'>
90
45105
1476
45454545454545454545
"""
```
<br/>

### 4. User Input
```python
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(a+b)
```
<br/>

### 5. String
```python
mystr = "This is a string"
print(len(mystr))
print(mystr)
print(mystr[4])
print(mystr[2:7])
print(mystr[2:9:2])
print(mystr[::])
print(mystr[::-1])
print(mystr.endswith("ing"))
print(mystr.count("i"))
print(mystr.capitalize())
print(mystr.upper())
print(mystr.lower())

"""
Output:- 

16
This is a string
 
is is
i sa
This is a string
gnirts a si sihT
True
3
This is a string
THIS IS A STRING
this is a string
"""
```
<br/>

### 6. List and Tuple
```python
mylst = ["Tanmay", "Tejas", "Parth", "Viraj"]
mynum = [5, 2, 6, 87, 1, 4]
print(mylst)
print(mylst[3])
print(mylst[0:3])
print(mynum)
mynum.sort()
mynum.reverse()
print(mynum)
print(min(mynum))
mynum.append(7)
print(mynum)
mynum.remove(6)
mynum.pop()
print(mynum)

mytp = (1, 6, 7)
print(type(mytp))

"""
Output:- 

['Tanmay', 'Tejas', 'Parth', 'Viraj']
Viraj
['Tanmay', 'Tejas', 'Parth']
[5, 2, 6, 87, 1, 4]
[87, 6, 5, 4, 2, 1]
1
[87, 6, 5, 4, 2, 1, 7]
[87, 5, 4, 2, 1]
<class 'tuple'>
"""
```
<br/>

### 7. Dictionary
```python
mydc = {
   "Tanmay": "Python",
   "Tejas": "C#",
   "Atharva": "C",
   "Yash": "C++",
   "nums": {"one": 1, "two": 2, "three": 3}
}
print(mydc)
print(mydc["Tanmay"])
mydc["Viraj"] = "AutoCAD"
print(mydc["nums"]["one"])
print(mydc)
del mydc["Atharva"]
print(mydc)
ydc = mydc.copy()
print(ydc.items())

"""
Output:- 

{'Tanmay': 'Python', 'Tejas': 'C#', 'Atharva': 'C', 'Yash': 'C++', 'nums': {'one': 1, 'two': 2, 'three': 3}}
Python
1
{'Tanmay': 'Python', 'Tejas': 'C#', 'Atharva': 'C', 'Yash': 'C++', 'nums': {'one': 1, 'two': 2, 'three': 3}, 'Viraj': 'AutoCAD'}
{'Tanmay': 'Python', 'Tejas': 'C#', 'Yash': 'C++', 'nums': {'one': 1, 'two': 2, 'three': 3}, 'Viraj': 'AutoCAD'}
dict_items([('Tanmay', 'Python'), ('Tejas', 'C#'), ('Yash', 'C++'), ('nums', {'one': 1, 'two': 2, 'three': 3}), ('Viraj', 'AutoCAD')])
"""
```
<br/>

### 8. Sets
```python
st1 = {2, 3, 4, 5}
st2 = {5, 6, 7}
st2.add(8)
print(st1, st2)
st3 = st1.intersection(st2)
print(st3)

"""
Output:- 

{2, 3, 4, 5} {8, 5, 6, 7}
{5}
"""
```
<br/>

### 9. Conditions
```python
val = int(input("Enter your age: "))
if val < 18:
    print("You cant drive")
elif val >= 18:
    print("You can drive")
else:
    print("Go to hell")

intp = int(input("Enter num: "))
print("Less") if intp <= 100 else print("Great")

"""
Output:- 

Enter your age: 12
You cant drive
Enter num: 34
Less
"""
```
<br/>

### 10. Loops
```python
friend = ["Viraj", "Parth", "Sandeep", "Rohan", "Vaishnav"]
nums = [["one", 1], ["two", 2], ["three", 3], ["four", 4]]
dict1 = dict(nums)
for name in friend:
    print(name)
for word, num in nums:
    print(word, num)
for word, num in dict1.items():
    print(word, num)
for i in range(0,10):
    print(i)
m = 0
while m < 10:
    print(m)
    m += 1

"""
Output:- 

Viraj
Parth
Sandeep
Rohan
Vaishnav
one 1
two 2
three 3
four 4
one 1
two 2
three 3
four 4
0
1
2
3
4
5
6
7
8
9
0
1
2
3
4
5
6
7
8
9
"""
```
<br/>

### 11. Break and Continue
```python
i=0
while(True):
    if i < 5:
        i+=1
        continue
    print(i)
    if i==44:
        break
    i+=1

"""
Output:- 

5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
"""
```
<br/>

### 12. Operators
```python
# Arithmetic
print(4+5)
print(8-6)
print(9/3)
print(5*2)
print(5//2)
print(5%2)
print(2**2)

# assignment
x = 5
x+=5
print(x)

# Comparison
print(5==5)

# Logical
a = True
b = False
print(a and b)

# identity
print(a is not b)

# membership
lst = [3, 4, 5, 6, 7]
print(5 in lst)

# bitwise
a = 0
b = 1
print(a&b)
print(a|b)

"""
Output:- 

9
2
3.0
10
2
1
4
10
True
False
True
True
0
1
"""
```

### 13. Functions
```python
def add(a:int, b:int):
    """Addition function"""
    c = a+b
    return c

print(add(4, 5))
print(add.__doc__)

"""
Output:- 

9
Addition function
"""
```
<br/>

### Exception Handling
```python
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a+b)
except Exception as e:
    print(e)

"""
Output:- 

Enter a number: r
invalid literal for int() with base 10: 'r'
"""
```
<br/>

### 15. File Handling
```python
f = open("15_file.txt", 'r')
content = f.read(19)
print(content)
content = f.read(10)
print(content)
f.close()

f = open("15_file.txt", 'r')
for l in f:
    print(l, end="")
f.close()

f = open("15_file.txt", 'r')
print(f.readline())
print(f.readline())
f.close()

f = open("15_file.txt", 'a')
f.write("\nHello\n")
f.close()

f = open("15_file.txt", 'r')
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0)
print(f.tell())
f.close()

with open("15_file.txt") as f:
    print(f.read())
```
<br/>

### 16. Global Variables
```python
def tan():
    x = 20
    def rock():
        global x
        x = 40
        print(x)
    print(x)
    rock()

tan()

"""
Output:- 

20
40
"""
```
<br/>

### 17. Recursion
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
```
<br/>

### 18. Lambda
```python
add = lambda a,b : a+b
print(add(5, 6))
```
<br/>

### 19. Fstring
```python
a = 10
print(f"statement {a}")
```
<br/>

### 20. Args and Kwargs
```python
def myfunc(normal, *args , **kwargs):
    print(normal)
    for i in args:
        print(i)
    for key , value in kwargs.items():
        print(key, value)
    
normal = "Tanmay"
args = ["Pizza", "Burgar", "Samosa", "Vada Pav", "Missal", "Dosa"]
kwargs = {
    "Tanmay": "Python",
    "Tejas": "C#",
    "Viraj": "AutoCAD",
    "Yash": "C++",
    "Atharva": "C" 
}

myfunc(normal, *args, **kwargs)

"""
Output:- 

Tanmay
Pizza
Burgar
Samosa
Vada Pav
Missal
Dosa
Tanmay Python
Tejas C#
Viraj AutoCAD
Yash C++
Atharva C
"""
```
<br/>

### 21. Enumerate
```python
lst = ["Pizza", "Burger", "Vada Pav", "Biryani", "Samosa"]

for index, item in enumerate(lst):
    if index%2==0:
        print(item)

"""
Output:- 

Pizza
Vada Pav
Samosa
"""
```
<br/>

### 22. Join
```python
lst = ["Pizza", "Burger", "Vada Pav", "Biryani", "Samosa"]
print(" , ".join(lst))

"""
Output:-

Pizza , Burger , Vada Pav , Biryani , Samosa
"""
```
<br/>

### 23. Map, Filter and Reduce
```python
# Map
nums = [1, 2, 3, 4, 5, 6, 7]
sq = list(map(lambda x: x*x, nums))
print(sq)

# Filter
num1 = [1, 2, 3, 4, 5, 6 ,7, 8, 9]
nlst = list(filter(lambda x: x>5, num1))
print(nlst)

# Reduce
from functools import reduce
num2 = [1, 2, 3, 4, 5]
nlst2 = reduce(lambda x, y: x+y, num2)
print(nlst2)

"""
Output:- 

[1, 4, 9, 16, 25, 36, 49]
[6, 7, 8, 9]
15
"""
```
<br/>

### 24. Decorators
```python
def dec1(func):
    def nowexec():
        print("Module starting")
        func()
        print("Ending")
    return nowexec

@dec1
def command():
    print("This is a test command")

command()

"""
Module starting
This is a test command
Ending
"""
```
<br/>

### 25. Classes
```python
class Student:
    pass

tanmay = Student()
viraj = Student()

tanmay.std = 12
tanmay.age = 18
print(tanmay.age)

"""
Output:- 

18
"""
```
<br/>

### 26. Constructor
```python
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def printdetails(self):
        print(f"{self.name} {self.age} {self.salary}")
emp1 = Employee("Tanmay", 27, 56000)
emp1.printdetails()

"""
Output:-

Tanmay 27 56000
"""
```
<br/>

### 27. Classmethod
```python
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
emp1 = Employee("Tanmay", 27, 56000)
emp1.printdetails()
print(emp1.no_of_leaves)
emp1.changeleaves(45)
print(emp1.no_of_leaves)

"""
Output:- 

Tanmay 27 56000
5
45
"""
```
<br/>

### 28. Staticmethod
```python
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

"""
Output:- 

Tanmay 27 56000
5
45
This is a Statement
"""
```
<br/>

### 29. Single Inheritance
```python
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

"""
Output:- 

Tanmay 18 None
"""
```
<br/>

### 30. Multiple Inheritance
```python
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

"""
Output:-

Tanmay 16 None
"""
```
<br/>

### 31. Multilevel Inheritance
```python
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

"""
Output:-

grandfather
father
son
"""
```
<br/>

### 32. Access Modifier
```python
class Employee:
    var = 34
    _myprotec = 5
    __protected = 45
obj = Employee()
print(obj.var)
print(obj._myprotec)
print(obj._Employee__protected)

"""
Output:-

34
5
45
tan
"""
```
<br/>

### 33. Super init
```python
class A:
    def __init__(self):
        self.var1 = "class A var1"
        self.var2 = "class A var2"
class B(A):
    def __init__(self):
        super().__init__()
obj = B()
print(obj.var1)

"""
Output:-

class A var1
"""
```
<br/>

### 34. Diamond Inheritance
```python
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

"""
Ouput:- 

D
"""
```
<br/>

### 35. Overloading
```python
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

"""
Ouput:-

9 + (9)i
4 + (5)i
"""
```
<br/>

### 36. Abstract Class
```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea():
        return 0
class Rectangle(Shape):
    def printarea():
        return 0
obj = Rectangle()
```
<br/>

### 37. Generator
```python
def gen(n):
    for i in range(n):
        yield i
g = gen(34)
print(g.__next__())
print(g.__next__())
print(g.__next__())

"""
Output:-

0
1
2
"""
```
<br/>

### 38. Comprehension
```python
print([i for i in range(100) if i%3 == 0])
print({i:f"item{i}" for i in range(1000) if i%100==0})

"""
Output:-

[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
{0: 'item0', 100: 'item100', 200: 'item200', 300: 'item300', 400: 'item400', 500: 'item500', 600: 'item600', 700: 'item700', 800: 'item800', 900: 'item900'}
"""
```