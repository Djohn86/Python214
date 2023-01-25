m = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]

for i in m:
    for j in i:
        print(j, end="\t\t")
    print()
print("\n\n\n")

for i in range(len(m[0])):
    for j in range(len(m)):
        print(m[j][i], end="\t\t")
    print()
