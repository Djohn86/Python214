b = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
for i in range(0, len(b)):
    a = 1
    for j in range(0, len(b)):
        if i != j and b[i] == b[j]:
            a = 0
            break
    if a:
        print(b[i], end=" ")



