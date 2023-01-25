def decor(fn):
    def wrap(*b):
        print('Среднее арифметическое чисел ', fn(*b) / len(b))

    return wrap


@decor
def sl(*lst):
    a = 0
    for i in lst:
        a += i
    print('Сумма чисел ', end='')
    print(*lst, sep=', ', end='')
    print(' = ', a)
    return a


sl(2, 3, 3, 4)
