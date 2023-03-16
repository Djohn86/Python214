# class Computer:
#     def __init__(self):
#         self.name = 'PC001'
#         self.os = self.OS()
#         self.CPU = self.CPU()
#
#
#     class OS:
#         def system(self):
#             return 'Windows 10'
#
#     class CPU:
#         def make(self):
#             return 'Intel'
#
#         def model(self):
#             return 'core i7'
#
#
#
# comp = Computer()
# print()


# class Base:
#     def __init__(self):
#         self.db = self.Inner
#
#     def display(self):
#         print('Метод базового класса')
#
#     class Inner(self):
#         def display1(self):
#             print('вложенный в базовый класс')
#
#
# class Subclass(Base):
#     def __init__(self):
#         print('in Subclass')
#         super.__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('Inner of Subclass')
#
#
# a = Subclass()
# a.display()


# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + ' спит')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + ' играет')
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + ' гавкает')
#
#
# beast = Dog('Baddy')
# beast.bark()
# beast.sleep()
# beast.play()


# class A:
#     def __init__(self):
#         print('init A')
#
#
# class B(A):
#     def __init__(self):
#         print('init B')
#
#
# class C(A):
#     def __init__(self):
#         print('init C')
#
#
# class D(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print('init D')
#
#
# d = D()
# print(D.mro())


# class Point:
#     def __init__(self, x ,y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# class Style:
#     def __init__(self, color='red', width=1):
#         print('Init style')
#         self.color = color
#         self.width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, color, width):
#         print('init Pos')
#         self.sp = sp
#         self.ep = ep
#         super().__init__(color, width)
#
#
# class Line(Pos, Style):
#     # def __init__(self,sp: Point, ep: Point, color='red', width=1):
#     #     Pos.__init__(self, sp, ep)
#     #     Style.__init__(color, width)
#
#     def draw(self):
#         print(f'РИсование линии: {self.ep}, {self.sp}, {self.color}, {self.width}')
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()


# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename ='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self,message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='log.txt')
#
#
# sub = MySubClass()
# sub.display('Эта строка будет напечатана и сохранена в файл')


# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec == other.sec
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# c4 = Clock(300)
# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")
# c1 = Clock(8000)
# print(c1.get_format_time())


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# cat = Cat('Пушок')
# print(cat)


# class Point:
#     def __init__(self, *args):
#         self.coord = args
#
#     def __len__(self):
#         return len(self.coord)
#
#
# p = Point(5, 7, 17)
# print(len(p))

from random import choice, randint

class Cat:
    def __init__(self, name, age, pol):
        self.name = name
        self.age = age
        self.pol = pol

    def __str__(self):
        if self.pol == 'M':
            return f'{self.name} is good boy'
        if self.pol == 'W':
            return f'{self.name} is good girl'
        else:
            return f'{self.name} is good kitty'

    def __repr__(self):
        return f'Cat(name="{self.name}f", age={self.age}, pol="{self.pol}" )'

    def __add__(self, other):
        if self.pol != other.pol:
            return [Cat('No name', 0, choice(['M', 'W'])) for _ in range(randint(1, 5))]
        else:
            raise TypeError('Типы не совместимы')


cat1 = Cat('Tom', 5, 'M')
cat2 = Cat('Elsa', 5, 'W')
print(cat1)
print(cat2)
print(cat1 + cat2)
