import random

s = [random.randrange(-20, 20) for i in range(10)]
print(s)
s.sort(reverse=True)
print(s)
