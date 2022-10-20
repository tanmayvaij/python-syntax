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