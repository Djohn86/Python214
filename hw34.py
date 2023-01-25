while True:
    print("1 - 'r' - применяет унарный минус к операнду\n2 - '+' - сложение\n3 - '-' - вычитание"
          "\n4 - '/' - деление\n5 - '*' - умножение\n6 - '%' - деление по модулю\n7 - '<' - минимальное из двух чисел"
          "\n8 - '>' - максимальное из двух чисел")
    oper = int(input("Выберите операцию: "))
    while not(1 <= oper <= 8):
        print("Нет такой операции")
        oper = int(input("Выберите операцию: "))
    if oper == 1:
        a = int(input("Введите число: "))
        print(a * (-1))
    else:
        b = int(input("Введите первое число: "))
        c = int(input("Введите второе число: "))
        if oper == 2:
            print(b + c)
        elif oper == 3:
            print(b - c)
        elif oper == 4:
            try:
                print(b / c)
            except ZeroDivisionError:
                print("На ноль делить нельзя!")
        elif oper == 5:
            print(b * c)
        elif oper == 6:
            if c != 0:
                print(b % c)
            else:
                print("На ноль делить нельзя!")
        elif oper == 7:
            print(b if b < c else c)
        elif oper == 8:
            print(b if b > c else c)
