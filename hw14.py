# 1я задача

# str1 = 'I am learning Python. hello, WORLD!'
#
# a = str1[:str1.find('h')]
# b = str1[str1.rfind('h')+1:]
# print(a+b)

# 2я задача

# str1 = 'I am learning Python. hello, WORLD!'
# a = str1[:str1.find('h')+1]
# b = str1[str1.rfind('h'):]
# c = str1[str1.find('h')+1:str1.rfind('h')]
#
# print(a + c[::-1] + b)

# 3я задача

# str1 = input("Введите строку: ")
# el1 = input("Введите заменяемую подстроку: ")
# el2 = input("Введите элемент для замены: ")
# print(str1.replace(el1, el2))

# 4я задача

# str1 = 'Ежевику для ежат принесли два ежа. Ежевику еле-еле ежата возле ели съели'
str1 = '''Ежевику для ежат
Принесли два ежа.
Ежевику еле-еле 
ежата возле ели съели'''
print(str1)
a = str1.split('\n')

s = 0
# print(a)
for i in a:
    k = i.split(' ')
    for j in k:
        if j[:1] == 'е' or j[:1] == 'Е':
            s += 1
print(s)
# for i in a:
#
#     for j in i:
#         print(j, end='')
#         if j[0] == 'е' or j[0] == 'Е':
#             # print(j[0])
#             s += 1
#
print('Количество слов, начинающихся с буквы "е": ', s)
