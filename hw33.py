a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
print("Максимальное значение: ", end = "")
print(a if b < a > c else b if a < b > c else c)

