try:
    number = int(input("Введите количество символов: "))
except ValueError:
    print("Вы ввели не целое число или строку! Введите целое число!")
    number = int(input("Введите количество символов: "))
sym = input("Введите символ: ")
print("0 - горизонтальная линия")
print("1 - вертикальная линия")
try:
    vector = int(input("Выберите направление: "))
except ValueError:
    print("Нельзя вводить строки!")
    vector = int(input("Выберите направление: "))
while not(0 <= vector <= 1):
    print("Нет такого направления")
    vector = int(input("Выберите направление: "))
i = 1
if vector == 0:
    while i <= number:
        print(sym,  end="")
        i += 1
else:
    while i <= number:
        print(sym)
        i += 1






