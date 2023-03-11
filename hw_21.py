from math import pi


class Sphere:
    def __init__(self, x, y, z,  r):
        self.__r = r
        self.__x = x
        self.__y = y
        self.__z = z

    def set_radius(self, r):
        self.__r = r

    def set_center(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def get_radius(self):
        return self.__r

    def get_volume(self):
        return (4/3) * pi * self.__r ** 3

    def get_square(self):
        return 4 * pi * self.__r ** 2

    def get_center(self):
        return self.__x, self.__y, self.__z

    def is_point_inside(self, x, y, z):
        return (x - self.__x) ** 2 + (y - self.__y) ** 2 + (z - self.__z) ** 2 < self.__r ** 2


s = Sphere(0, 0, 0, 0.6)
# s.set_radius(0.6)
print('Радиус сферы равен: ', s.get_radius())
print('Объём сферы равен: ', s.get_volume())
print('Площадь сферы равен: ', s.get_square())
print('Центр сферы: ', s.get_center())
print(s.is_point_inside(0, 1.5, 0))
s.set_radius(1.6)
print(s.is_point_inside(0, 1.5, 0))
