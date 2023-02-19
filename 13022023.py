from random import randint
import time


# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j+1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#         #     print(*array)
#         # print("=================")
#
# lst = [randint(1, 99) for i in range(10000)]
#
# print(lst)
# bubble(lst)
# start = time.monotonic()

# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# lst = [randint(1, 99) for i in range(10000)]
# start = time.monotonic()
# bubble(lst)
# res = time.monotonic() - start
# print(round(res, 3), 'sec')

# def marge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#
#     left = marge_sort(a[:n//2])
#     right = marge_sort(a[n//2: n])
#
#     i = j = 0
#     res = []
#
#     while i < len(left) or j < len(right):
#         if not i < len(left):
#             res.append(right[j])
#             j += 1
#         elif not j < len(right):
#             res.append(left[i])
#             i += 1
#         elif left[i] < right[j]:
#             res.append(left[i])
#             i +=1
#         else:
#             res.append(right[j])
#             j += 1
#     return res
#
#
# # array = [8, 2, 6, 4, 5]
# array = [randint(1, 1000) for i in range(10000)]
# start = time.monotonic()
# print(array)
# array = marge_sort(array)
# res = time.monotonic() - start
# print(array)
# print(round(res, 3), 'sec')



# def shel_sort(s):
#     gap = len(a)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#         gap //= 2
#     return s
#
#
# a = [randint(1, 99) for i in range(10000)]
# start = time.monotonic()
# # print(a)
# shel_sort(a)
# res = time.monotonic() - start
# # print(a)
# print(round(res, 3), 'sec')



# def fast_sort(a):
#     if len(a) > 1:
#         x = a[(len(a) - 1)//2]
#
#         low = [i for i in a if i < x]
#         eq = [i for i in a if i == x]
#         hi = eq = [i for i in a if i > x]
#         a = fast_sort(low) + eq + fast_sort(hi)
#
#     return a
#
#
# lst = [9, 5, -3, 4, 7, 8, -8]
# print(lst)
# lst = fast_sort(lst)
# print(lst)

# f = open('text1.txt', mode='r')
# print(*f)
# print(f)
# f.close()

# f = open('text1.txt')
# print(f.read(3))
# print(f.read())
# f.close()

f = open('test.txt')
count = 0

# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# print(f.readlines(16))
for line in f:
    count += 1
print(count)
f.close()
