# import os
#
# dir_name = 'global'
#
# objs = os.listdir(dir_name)
# print(objs)
#
# for i in objs:
#     p = os.path.join(dir_name, i)
#     print(p)
#     if os.path.isfile(p):
#         print(f"{i} - file - {os.path.getsize(p)} bytes")
#     elif os.path.isdir(p):
#         print(f"{i} - dir")


# class Point:
#     """Класс координат"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
#
# Point.x = 100
# p1.x = 20
# p1.y = 30
#
# p2 = Point()
# print(p2.x, p2.y)
# print(p1.x, p1.y)
# print(type(p1))
# print(dir(Point))
# print(Point.__doc__)
#
# print(p1.__dict__)
# print(p2.__dict__)
# print(Point.__dict__)


# class Point:
#     """Класс координат"""
#     x = 1
#     y = 1
#
#     def set_cord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 20
# # p1.y = 17
# p1.set_cord(5, 10)

# p2 = Point()
# p2.x = 12
# p2.y = 65
#
# Point.set_cord(p1)
# Point.set_cord(p2)


# class Human:
#     name = 'name'
#     birth = '00.00.0000'
#     phone = '00-00-00'
#     country = 'count'
#     city = 'city'
#     address = 'street'
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДень рождения: {self.birth}\nТелефон: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.city}\nАдрес: {self.address}\n")
#
#         print('=' * 40)
#
#
#     def input_info(self, first, birthday, phone, country, city, addres):
#         self.name = first
#         self.birth = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = addres
#
#     def
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         print('Экземпляр класса создан!')
#
#     def __del__(self):
#         print("Экземпляр класса удален")
#
#
#
#
# p1 = Point(5, 10)
# print(p1.x, p1.y)
# # del p1
# p1 = 5
# print(p1.__dict__)


# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.count += 1
#
#
# p1 = Point(5, 10)
# p2 = Point(21, 30)
# p3 = Point(12, 54)
# print(Point.count)
# print(p1.count)


# class Robot():
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f'Инициализация робота: {self.name}')
#         Robot.count += 1
#
#     def __del__(self):
#         print(self.name, 'выключается!!!')
#         Robot.count -= 1
#
#     def hi(self):
#         print(f"Приветствую! Меня зовут: {self.name}")
#
#
# droid1 = Robot("R2-D2")
# droid1.hi()
# print(f"Численность роботов: {Robot.count}")
#
# droid2 = Robot("C-3PO")
# droid2.hi()
# print(f"Численность роботов: {Robot.count}")
#
# print('\nЗдесь роботы могут работать\nРоботы закончили работу. Выключаем их')
#
# del droid1
# del droid2
# print(f"Численность роботов: {Robot.count}")


# class Point:
#     """Класс координат"""
#     def __init__(self,x ,y):
#         self.__x = x
#         self.__y = y
#
#
# p1 = Point(5, 10)
# # print(p1.__x, p1.__y)
# p1.__x = 100
# # p1.y = 'abc'
# print(p1.__dict__)


class Translate:
    def __init__(self, kg):
        self.__kg = kg

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg(int, float)):
            self.__kg = new_kg
        else:
            print("Килограммы задаются числами")

    def to_pounds(self):
        return self._kg * 2.205


weight = Translate(12)
print(weight.kg, )
