# print('py'. center(11, '+'))
# print("    py". lstrip())
# print("py      ".rstrip())
# print('https://www.youtube.com/watch?v=9eVNw1NZZe0&list=PL-Hq_KrfJ31WQbkU99U-78JWCixpNlS4v&index=78'.
#       lstrip('https://'))
#
#
# print('https://www.pythin.orgw'.strip('/:httporgw.'))
# print('https://www.pythin.orgw'.lstrip('/:https').rstrip('org.w'))

# s = 'Hello world. I am learinig python'
#
# print(s.startswith('I am', 14))
# print(s.endswith('on.'))


# str1 = "Я изучая Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace(('Nython', 'Python', 2)))



# s = 'Замените в этой строке все появления буквы "о" на букву "0", кроме первого и последнего вхождения'
#
# v1 = s[:s.find('о')+1]
# v2 = s[s.find('о')+1:s.rfind('о')]
# v3 = s[s.rfind('о'):]
# print(v1)
# print(v2)
# print(v3)
# print(v1 + v2.replace('о', 'O', ) + v3)


# s = '-'
# r = ('a', 'b', 'c')
# print(s.join(r))
#
# print('..'.join(['1', '99']))
# print(':'.join('Hello'))
#
#
# print('Строка разделенная пробелами'.split())
# print('www.python.org'.split('.'))
#
# print('www.python.org'.split('.', 1))
# print('www.python.org'.rsplit('.', 1))
#
# l = input('-->').split()
# print(l)

# l = input('-->').split()
# l = list(map(int.l))
# print(l)

# l = input('Ведите фамилию , имя и отчество: ').split()
# print(f'{l[0]} {l[1][0]}.{l[2][0]}.')


# Регулярные выражения

import re

# print(dir(re))

# s = "Я ищу совпадения в 2003 году. И я найду их в два счёта."
# reg = "я"
# reg1 = 'совпадения'
# reg2 = 'Я ищу'
# print(re.findall(reg, s))
# print(re.search(reg1, s))
# print(re.search(reg1, s).span())
# print(re.search(reg1, s).start())
# print(re.search(reg1, s).end())
# print(re.search(reg1, s).group())
# print(re.match(reg2, s))
#
# reg3 = r'\.'
# print(re.split(reg3, s))
#
# print(re.sub(reg3, '!', s, 1))



s = "Я ищу совпадения в 2023 году. И я найду их в два счёта. - 9875[]  2000222"

# reg = '2[0-9][0-9][0-9]'
# reg2 = r'[А-яЁё.\[\]-]'
# print(re.findall(reg, s))
# print(re.findall(reg2, s))
# print(ord("е"))
# print(ord("ё"))

# reg3 = r'[^А - я]'
# print(re.findall(reg3, s))
# reg4 = r'.[^2]'
# print(re.findall(reg4, s))


# s1 = 'Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09. '
# rg = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(rg, s1))


# reg = r'20*'
# print(re.findall(reg, s))
#
#
# d = 'Цифры: 7, +17, -42, 0012, 0.3'
#
# print(re.findall(r'[+-]?[\d.]+', d))

#
# d = '05-03-1987 # Дaта рождения'
# print('Дата рождения', re.sub(r"#.*", "", d))
# print('Дата рождения', re.sub('-', '.', re.sub(r"#.*", "", d)))

# s = 'author=Пушкин А.С,; title = Евгений Онегин; price =200; year= 1831'
# # reg = r'\w+\s*=\s*\w+\s*[\w.]'
# reg = r'\w+\s*=[^;]+'
# print(re.findall(reg, s))

# s1 = '12 декабря 2023 года'
# reg = r'\d{2,4}'
# print(re.findall(reg, s1))


# s = '+7 499 456-65-78, +74999451235, 7 (499) 456 45 79, 74998005060'
# reg = r'\+?7\d{10}'
# print(re.findall(reg, s))


# print('py'. center(11, '+'))
# print("    py". lstrip())
# print("py      ".rstrip())
# print('https://www.youtube.com/watch?v=9eVNw1NZZe0&list=PL-Hq_KrfJ31WQbkU99U-78JWCixpNlS4v&index=78'.
#       lstrip('https://'))
#
#
# print('https://www.pythin.orgw'.strip('/:httporgw.'))
# print('https://www.pythin.orgw'.lstrip('/:https').rstrip('org.w'))

# s = 'Hello world. I am learinig python'
#
# print(s.startswith('I am', 14))
# print(s.endswith('on.'))


# str1 = "Я изучая Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace(('Nython', 'Python', 2)))



# s = 'Замените в этой строке все появления буквы "о" на букву "0", кроме первого и последнего вхождения'
#
# v1 = s[:s.find('о')+1]
# v2 = s[s.find('о')+1:s.rfind('о')]
# v3 = s[s.rfind('о'):]
# print(v1)
# print(v2)
# print(v3)
# print(v1 + v2.replace('о', 'O', ) + v3)


# s = '-'
# r = ('a', 'b', 'c')
# print(s.join(r))
#
# print('..'.join(['1', '99']))
# print(':'.join('Hello'))
#
#
# print('Строка разделенная пробелами'.split())
# print('www.python.org'.split('.'))
#
# print('www.python.org'.split('.', 1))
# print('www.python.org'.rsplit('.', 1))
#
# l = input('-->').split()
# print(l)

# l = input('-->').split()
# l = list(map(int.l))
# print(l)

# l = input('Ведите фамилию , имя и отчество: ').split()
# print(f'{l[0]} {l[1][0]}.{l[2][0]}.')


# Регулярные выражения

import re

# print(dir(re))

# s = "Я ищу совпадения в 2003 году. И я найду их в два счёта."
# reg = "я"
# reg1 = 'совпадения'
# reg2 = 'Я ищу'
# print(re.findall(reg, s))
# print(re.search(reg1, s))
# print(re.search(reg1, s).span())
# print(re.search(reg1, s).start())
# print(re.search(reg1, s).end())
# print(re.search(reg1, s).group())
# print(re.match(reg2, s))
#
# reg3 = r'\.'
# print(re.split(reg3, s))
#
# print(re.sub(reg3, '!', s, 1))



s = "Я ищу совпадения в 2023 году. И я найду их в два счёта. - 9875[]  2000222"

# reg = '2[0-9][0-9][0-9]'
# reg2 = r'[А-яЁё.\[\]-]'
# print(re.findall(reg, s))
# print(re.findall(reg2, s))
# print(ord("е"))
# print(ord("ё"))

# reg3 = r'[^А - я]'
# print(re.findall(reg3, s))
# reg4 = r'.[^2]'
# print(re.findall(reg4, s))


# s1 = 'Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09. '
# rg = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(rg, s1))


# reg = r'20*'
# print(re.findall(reg, s))
#
#
# d = 'Цифры: 7, +17, -42, 0012, 0.3'
#
# print(re.findall(r'[+-]?[\d.]+', d))

#
# d = '05-03-1987 # Дaта рождения'
# print('Дата рождения', re.sub(r"#.*", "", d))
# print('Дата рождения', re.sub('-', '.', re.sub(r"#.*", "", d)))

# s = 'author=Пушкин А.С,; title = Евгений Онегин; price =200; year= 1831'
# # reg = r'\w+\s*=\s*\w+\s*[\w.]'
# reg = r'\w+\s*=[^;]+'
# print(re.findall(reg, s))

# s1 = '12 декабря 2023 года'
# reg = r'\d{2,4}'
# print(re.findall(reg, s1))


# s = '+7 499 456-65-78, +74999451235, 7 (499) 456 45 79, 74998005060'
# reg = r'\+?7\d{10}'
# print(re.findall(reg, s))


