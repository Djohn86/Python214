def mkr(s):
    a = []
    for i in s:
        if i % 13 == 0 and i > 0:
            a.append(i)
    if len(a) > 0:
        p = max(a)
    else:
        p = "такого числа не существует"
    return p


print(mkr([2, 7, 0, 3, 1, 5, -13]))
print(mkr([2, 7, 0, 3, 1, 5, -13, 13]))
print(mkr([26]))
print(mkr([99, 99, 100, 34, -39]))
print(mkr([99, 39, 99, 100, 34]))
