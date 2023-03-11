# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#         print('Base class')
#
#     def get_width(self):
#         return  self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print('Переопределенный инициатор Line')
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f'Рисование линии:  {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f'Рисование прямоугольника:  {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# # print(line._width)
# line.draw_line()
# rect = Rect(Point(20, 35), Point(70, 60))
# rect.draw_rect()


class Figure:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c


class Rectangle(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.__width = width
        self.__height = height

    def area(self):
        print(f'Площадь {self.color} прямокгольника:')
        return self.__width * self.__height


rect = Rectangle(10, 20, 'green')
print(rect.area())


