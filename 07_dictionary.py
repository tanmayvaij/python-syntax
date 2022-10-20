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