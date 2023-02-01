# def fun(s, c_old, c_new):
#     s2 = ""
#     for i in range(len(s)):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#     return s2
#
#
# str1 = "Я изучая Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = fun(str1, 'N', 'P')
# print(str1)
# print(str2)


# print(u"Привет")
# print("Привет")

# print(r"C:folder\file.txt")

# from math import pi
#
# name = 'Dmitriy'
# age = 24
# print(f'Меня зовут {name}. Мне {age} лет')
# print(f'Значение симла pi: {round(pi,2)}')
# print(f'Значение симла pi: {pi:.2f}')
#
#
# x = 5
# e = 10
# print(f'{x} x {y}')

# a = 74
# print(f'{{{{{a}}}}}')


# dir_name = 'my doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')

#
# x = """<div>
#     <p>Text</p>
# <div>
# """

# print(x)

#
# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n**2
#
# print(square(4))
#
# print(square.__doc__)


# import math
#
# def cilinder(r, h):
#     """"
#     Вычисляет площадь цилиндра
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: Положительное число радиуса основания цилиндра
#     :param h: Положительное число, высота цилиндра
#     :return: Положительное число, плрщадь цилиндра
#     """
#     return 2*math.pi*r*(r+h)
#
# print(cilinder(2, 4))
# print(cilinder.__doc__)

# print(ord('a'))

# while True:
#     n = input("-->")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


# a = 122
# b = 97
#
# if a > b:
#     a, b = b, a
# for i in range(a, b + 1):
#     print(chr(i), end=' ')

# print('apple' == 'Apple')
# print('apple' > "Apple")
# print(ord('a'))
# print(ord('A'))
# print(9 > 5)
# print(ord('0'))
# print(ord('9'))
# print(ord('5'))

# from random import randint
#
# def rand_pas():
#     rand_len = randint(7, 10)
#     res = ''
#
#     for i in range(rand_len):
#         rand_char = chr(randint(53, 126))
#         res += rand_char
#     return res
#
# print("Ваш случайный пароль: ", rand_pas())



# print(dir(str))


# s = 'Hello WORLD! I am learning python'
# # print(s.capitalize())
# # print(s.lower())
# # print(s.upper())
# # print(s.swapcase())
#
# print(s.count('h', 0, -4))
#
# print(s.find('e'))
# print(s.rfind('e'))

# s = 'один два'
#
# s = s[s.find(' ') + 1:] + ' ' + s[:s.find(' ')]
# print(s)


# s = 'ab12c59p7dq'
#
# d = []
# for i in s:
#     if '013456789'.find(i) != -1:
#         d.append(int(i))
# # d = list(filter(lambda x: '0' <= x <= '9', s))
# # d = [i for i in s if i in '0123456789']
#
#
# print(d)
