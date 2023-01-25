# 1
# from math import pi
#
# print('Площадь окружности радиуса 2: ', (lambda r: pi * r ** 2)(2))
# print('Площадь прямоугольника: ', (lambda r, x: x * r)(10, 13))
# print('Площадь трапеции: ', (lambda a, b, h: h * ((a + b)/2))(5, 7, 3))


# 2

# print((lambda a, b, c: a * b * c)(2, 5, 5))

# 3

# s = [
#     {'name': 'Jenifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nicolas', 'final': 98}
# ]

# print(sorted(s, key=lambda x: x['name']))
# print(sorted(s, key=lambda x: x['final'], reverse=True))


# 4

# s = [
#     {'name': 'Jenifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nicolas', 'final': 98}
# ]
#
# print(max(s, key=lambda x: x['final']))
# print(min(s, key=lambda x: x['final']))

# 5

# s = [3, 6, 8, 9, 1, 2]
#
#
# s2 = list(map(lambda a, b: a * b**3, s, range(len(s))))
#
# print(s2)

# 6

nums = [3, 5, 7, 3, 9, 5, 7, 2]

print(list(map(lambda a: a**2, nums)))
print(list(map(lambda a: a**3, nums)))
