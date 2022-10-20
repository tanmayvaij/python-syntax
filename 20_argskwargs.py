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