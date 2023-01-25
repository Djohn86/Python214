from math import sqrt, pi

ch = int(input("Выбор фигуры: \n1 - треугольник\n2 - прямоугольник\n3 - круг\n--> " ))
if ch == 1:
    a = int(input("Введите сторону А: "))
    b = int(input("Введите сторону B: "))
    c = int(input("Введите сторону C: "))
    pr = (a + b + c)/2
    s = sqrt(pr * (pr - a) * (pr - b) * (pr - c))
    print("Площадь треугольника равна", round(s, 3))
if ch == 2:
    a = int(input("Введите сторону А: "))
    b = int(input("Введите сторону B: "))
    s = a * b
    print("Площадь прямоугольника равна", s)
if ch == 3:
    r = int(input("Введите радиус круга: "))
    s = pi * r ** 2
    print("Площадь круга равна", round(s, 3))



