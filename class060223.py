import re

# print(re.findall(r'\w', '12 + й'))
# print(re.findall(r'\w', '12 + й', flags=re.ASCII))
#
# text = 'Hello world'
# print(re.findall(r'\w\+', text, re.DEBUG))

# s = 'Я ищу совпадения в 2023'
# reg = 'я'
# print(re.findall(reg, s, re.IGNORECASE))
#
# text = """
# one
# two
# """
#
# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))

# print(re.findall(('''
# [a-z.-]+
# @
# [a-z.-]+
# ''', "test@mail.ru", re.VERBOSE)))


# text = """Python,
# python,
# PYTHON
# """
# reg = "(?mi)^python"
# print(re.findall(reg, text))

# def valid_name(name):
#     return re.findall("[a-z0-9_-]{3,16}]", name, re.I)
#
#
# print(valid_name('Python_master'))
# print(valid_name('Pyt'))


# text = '<body>Пример жадного соответствия регулярных выражений</body>'
# print(re.findall('<.*?>', text))

s = '<p>Изображение <img src ="bg.jpg"> - фон страницы</p>'
# preg = '<img.*?>'
reg = '<img\s+[^>]*'
print(re.findall(reg, s))
