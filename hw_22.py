from math import sqrt


class Pair:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def set_data1(self, a):
        self._a = a

    def set_data2(self, b):
        self._b = b

    def get_sum(self):
        return self._a + self._b

    def get_mult(self):
        return self._a * self._b


class RightTriangle(Pair):

    def hyp(self):
        return round(sqrt(self._a ** 2 + self._b ** 2), 2)

    def desc(self):
        return self._a, self._b, self.hyp()

    def square(self):
        return (self._a * self._b) / 2


c = Pair(5, 8)
c1 = RightTriangle(5, 8)
print("Гипотенуза треугольника ABC: ", c1.hyp())
print("Прямоугольный треугольник ABC: ", c1.desc())
print("Площадь треугольника ABC: ", c1.square())
print()
print("Сумма: ", c.get_sum())
print("Произведение: ", c.get_mult())

c1.set_data1(10)
c1.set_data2(20)
print("Гипотенуза треугольника ABC: ", c1.hyp())
print("Прямоугольный треугольник ABC: ", c1.desc())
print("Площадь треугольника ABC: ", c1.square())
print()
print("Сумма: ", c1.get_sum())
print("Произведение: ", c1.get_mult())
