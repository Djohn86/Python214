import random

s = [random.randrange(0, 50) for i in range(10)]
# s = [12, 15, 18, 91, 18]
print(s)
c = min(s)
print(c)
ind = s.index(c)
print(ind)
if ind != 0:
    del s[0: ind]
print(s)
