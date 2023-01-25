# def square(a, b, c):
#     def fun(x, y):
#         return x * y
#
#     s = 2 * (fun(a, b) + fun(b, c) + fun(a, c))
#
#     print(s)
#
#
# square(2, 4, 6)
# square(5, 8, 2)
# square(1, 6, 8)


# s = None
#
#
# def square(a, b, c):
#     def fun(x, y):
#         return x * y
#
#     global s
#
#     s = 2 * (fun(a, b) + fun(b, c) + fun(a, c))
#
#     print(s)
#
#
# square(2, 4, 6)
# square(5, 8, 2)
# square(1, 6, 8)


def square(a, b, c):
    s = 0

    def fun(x, y):
        nonlocal s
        s += x * y

    fun(a, b)
    fun(a, c)
    fun(c, b)

    print(2 * s)


square(2, 4, 6)
square(5, 8, 2)
square(1, 6, 8)
