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

str1 = 'Ежевику для ежат принесли два ежа. Ежевику еле-еле ежата возле ели съели'
print(str1)
a = str1.split(' ')
s = 0
for i in a:
    if i[0] == 'е' or i[0] == 'Е':
        s += 1

print('Количество слов, начинающихся с буквы "е": ', s)
