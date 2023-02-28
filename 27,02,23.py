# class Counter:
#
#
#     @staticmethod
#     def max_counter(a, b, c, d):
#         return max(a, b, c, d)
#
#     @staticmethod
#     def min_counter(a, b, c, d):
#         return min(a, b, c, d)
#
#     @staticmethod
#     def q_counter(*args):
#         return sum(args) / len(args)
#
#     @staticmethod
#     def f_counter(x):
#         count = 1
#         for i in range(1, x + 1):
#             count *= i
#         return count
#
#
# print(Counter.max_counter(3, 5, 7, 9))
# print(Counter.min_counter(3, 5, 7, 9))
# print(Counter.q_counter(3, 5, 7, 9))
# print(Counter.f_counter(5))

# import math
#
# class Area:
#     @staticmethod
#     def treagle(a, b, c):
#         p = (a + b + c) / 2
#         return math.sqrt(p*(p-a)*(p-b)*(p-c))
#
#     @staticmethod
#     def treagle2(a, h):
#         return 0.5 * a * h
#
#     @staticmethod


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         return cls(day, month, year)
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# date = Date.from_string('26.02.2023')
# print(date.string_to_db())
# date = Date.from_string('10.05.2023')
# print(date.string_to_db())