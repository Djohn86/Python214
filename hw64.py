from random import randint

m = [[randint(0, 10)for i in range(6)]for j in range(6)]
for i in m:
    for j in i:
        print(j, end="\t\t")
    print()
print()
m[0], m[1] = m[1], m[0]
m[2], m[3] = m[3], m[2]
m[4], m[5] = m[5], m[4]
for i in m:
    for j in i:
        print(j, end="\t\t")
    print()