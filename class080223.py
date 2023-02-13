# Рекурсия

# def elevator(n):
#     if n == 0:
#         print('Вы в подвале')
#         return
#     print('-->', n)
#     elevator(n - 1)
#     print(n, end=' ')
#
#
# n1 = int(input('На каком вы этаже: '))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(254, 16))

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]

# print(isinstance(names[1], list))
# print(names)

# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
# print(count_items(names))


# count = 0
# for i in names:
#     if isinstance(i, list):
#         for j in i:
#             if isinstance(j, list):
#                 for k in j:
#                     count += 1
#             else:
#                 count += 1
#     else:
#         count += 1
#
#
# print(count)


# def union(s):
#     if not s:
#         return s
#     if isinstance(s[0], list):
#         return union(s[0] + union((s[1:])))
#     return s[:1] + union(s[1:])
#
#
# print(union(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == '\t' or text[0] == ' ':
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove('Hello\tWorld! '))


# def search(s, item):
#     found = False
#     pos = 0
#     while pos < len(s) and not found:
#         if s[pos]  == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# lst.sort()
# print(lst)
# print(search(lst, 13))
# print(search(lst, 3))

# a = ['a', 'b']
# c = ['c', 'd',['k', 'l']]
# s = a + c
# print(s)

names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert", "yyy"], "Alex", ["Bea", "Bill", 'lll'], "Ann", ['ggg', 'rrr']]
count = 0
while len(names) != 0:
    k = []
    for i in range(len(names)):
        if type(names[i]) == list:
            k += names[i]
        else:
            count += 1
    names = k

print(count)
