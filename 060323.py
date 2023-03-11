# class Vector(list):
#     def __str__(self):
#         return ' '.join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))


from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print('Нарисовать шахматную фигуру')
#
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Queen(Chess):
#     def move(self):
#         print('Ферзь перемещен на позицию')
#
#
# # q = Chess()
# q = Queen()
# q.draw()
# q.move()

# from math import pi
#
class Table:
    def __init__(self, width =None, length=None, radius=None):
        if radius is None:
            self.width = width
            self.length = length
        else:
            self._radius = radius

    def calc_area(self):
        raise NotImplementedError('В дочернем классе должен быть определен метод calc_area()')


class SqTable(Table):
    def calc_area(self):
        return self._width * self._length


class RoundTable(Table):
    def calc_area(self):
        return round(pi * self._radius ** 2)


t = Table(20, 10)
print(t.__dict__)
print(t.calc_area())
t1 = Table(radius=20)