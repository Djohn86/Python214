# import  math
#
# class Point:
#     __slots__ = ('x', 'y', '__z')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.z = math.sqrt(x*x + y*y)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         self.__z = value
#
#
# class Point2D:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.z = math.sqrt(x*x + y*y)
#
#
# p1 = Point(5, 10)
# # print(p1.z)
# # p1.z = 10
# # print(p1.__dict__)
# p2 = Point2D(5, 8)
# print('p1 =', p1.__sizeof__())
# print('p2 =', p2.__sizeof__() + p2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#
# p3 = Point3D(10, 300)
# p3.z = 30
# print(p3.x, p3.y, p3.z)
# # print(p3.__dict__)


# Функторы

# class Count:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Count()
# c1()
# c1()
# c1()
# c1()
# c2 = Count()
# c2()
# c2()
# c2()


# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str) or not isinstance(chars, str):
#             raise ValueError('Аргументы должны быть строкой')
#         return string.strip(chars)
#     return wrap
#
#
# c1 = string_strip(",.<>!:;")
# print(c1(" !Hello world?; "))
#
#
# class StringStrip:
#     def __init__(self, char):
#         self.__char = char
#
#     def __call__(self, string):
#         if not isinstance(string, str) or not isinstance(self.__char, str):
#             raise ValueError('Аргументы должны быть строкой')
#
#         return string.strip(self.__char)
#
#
# s2 = StringStrip(",.<>!:;")
# print(s2(" !Hello world?; "))


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('ФФФФФ')
#         self.func()
#         print('lijuihuih')
#
#
# @MyDecorator
# def func():
#     print('Hello')
#
#
# func()


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
# @Power
# def func(a, b):
#     return a * b
#
#
# print(func(2, 3))


# class MyDecorator:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             print('перед функцией')
#             print(self.arg)
#             func(a, b)
#             print('после функции')
#
#         return wrap
#
#
# @MyDecorator('text2')
# def func1(a, b):
#     print(a, b)


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def info(self):
        print(f'{self.name} {self.surname}')


p1 = Person("Виталий", "Карасев")
p1.info



