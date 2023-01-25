w = 8
h = 8
for i in range(h):
    for j in range(w):
        if j <= h - 1 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
