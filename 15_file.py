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