val = int(input("Enter your age: "))
if val < 18:
    print("You cant drive")
elif val >= 18:
    print("You can drive")
else:
    print("Go to hell")

intp = int(input("Enter num: "))
print("Less") if intp <= 100 else print("Great")