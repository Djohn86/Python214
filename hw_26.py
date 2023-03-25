class Check:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Значение стороны треугольника должно быть положительным')
        elif not isinstance(value, int):
            raise ValueError('Значение должно быть целым')
        instance.__dict__[self.name] = value


class Triangle:
    a = Check()
    b = Check()
    c = Check()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def real(self):
        if self.a + self.b > self.c and self.a < self.b + self.c and self.a + self.c > self.b:
            print(f'Треугольник со сторонами {self.a}, {self.b}, {self.c} существует')
        else:
            print(f'Треугольник со сторонами {self.a}, {self.b}, {self.c} не существует')


t1 = Triangle(2, 5, 6)
t2 = Triangle(5, 2, 8)
t3 = Triangle(7, 3, 6)
t1.real()
t2.real()
t3.real()

