class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def vis(self):
        return f'{self.x}, {self.y}, {self.z}'

    def __add__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.x + other.x, self.y + other.y, self.z + other.z

    def __sub__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.x - other.x, self.y - other.y, self.z - other.z

    def __mul__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.x * other.x, self.y * other.y, self.z * other.z

    def __truediv__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.x / other.x, self.y / other.y, self.z / other.z

    def __eq__(self, other):
        if not isinstance(other, Point3D):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")

        return self.x == other.x and self.y == other.y and self.z == other.z

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")

        if item == 'x':
            return self.x
        elif item == 'y':
            return self.y
        elif item == 'z':
            return self.z

        return 'Неверный ключ'

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")

        if not isinstance(value, int):
            raise ValueError("Значение должно быть целым числом")

        if key == 'x':
            self.x = value
        elif key == 'y':
            self.y = value
        elif key == 'z':
            self.z = value


c1 = Point3D(12, 15, 18)
c2 = Point3D(6, 3, 9)
print('Координаты 1-й точки:', c1.vis())
print('Координаты 2-й точки:', c2.vis())
c3 = c1 + c2
c4 = c1 - c2
c5 = c1 * c2
c6 = c1 / c2
print("Сложение координат: ", c3)
print("вычитание координат: ", c4)
print("Умножение координат: ", c5)
print("Деление координат: ", c6)
print('Равенство координат: ', c1 == c2)
print('x =', c1['x'], 'x1 =', c2['x'])
print('y =', c1['y'], 'y1 =', c2['y'])
print('z =', c1['z'], 'z1 =', c2['z'])
c1['x'] = int(input('Введите значение 1-й точки для  координаты x: '))
c1['y'] = int(input('Введите значение  1-й точки для координаты y: '))
c1['z'] = int(input('Введите значение  1-й точки для координаты z: '))
c2['x'] = int(input('Введите значение  2-й точки для координаты x: '))
c2['y'] = int(input('Введите значение 2-й точки для координаты y: '))
c2['z'] = int(input('Введите значение 2-й точки для координаты z: '))
print('x =', c1['x'], 'x1 =', c2['x'])
print('y =', c1['y'], 'y1 =', c2['y'])
print('z =', c1['z'], 'z1 =', c2['z'])
