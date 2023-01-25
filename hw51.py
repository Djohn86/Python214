from random import randrange

s = [randrange(0, 151) for i in range(10)]
c = max(s)
print(s)
s.remove(c)
print(s)
print(c)
s.insert(0, c)
print(s)



