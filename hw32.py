# n = int(input("Введите количество символов: "))
# i = 1
# while i < 6:
#     if i % 2 == 1:
#         print("+" * n)
#     else:
#         print("-" * n)
#     i += 1

n = int(input("Введите количество символов: "))
line = int(input("Введите количество строк: "))
i = 1
while i <= line:
    print("+" * n)
    j = 1
    while j < 2:
        print("-" * n)
        j += 1
    i += 1
