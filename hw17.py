# 1-я задача

s = [-2, 3, 8, -11, -4, 6]


def otr(x):
    if not x:
        return 0
    else:
        count = otr(x[1:])
        if x[0] < 0:
            count += 1
    return count


print('Количество отрицательных чисел: ', otr(s))

# 2-я задача

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert", "yyy"], "Alex", ["Bea", "Bill", 'lll'], "Ann", ['ggg', 'rrr']]
# count = 0
# while len(names) != 0:
#     k = []
#     for i in range(len(names)):
#         if type(names[i]) == list:
#             k += names[i]
#         else:
#             count += 1
#     names = k
#
# print(count)
