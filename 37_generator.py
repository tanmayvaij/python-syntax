def gen(n):
    for i in range(n):
        yield i
g = gen(34)
print(g.__next__())
print(g.__next__())
print(g.__next__())