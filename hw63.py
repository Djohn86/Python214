from random import randint

m = [[randint(0, 10)for i in range(6)]for j in range(6)]
for i in m:
    for j in i:
        print(j, end="\t\t")
    print()
print()
a = []
for c in range(6):
    k = randint(0, 10)
    a.append(k)
    print(k, end="\t\t")
print()

for i in range(len(m)):
    if i % 2 == 0:
        m[i] = a
print()
for i in m:
    for j in i:
        print(j, end="\t\t")
    print()
print()



