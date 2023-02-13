import re

# 1я задача

s = 'my-p@ssw0rd'
s1 = 'Passw'
s2 = 'jk532ywp@-partner'
reg = '[A-Za-z0-9@-]{6,18}'
print(bool(re.findall(reg, s)))
print(bool(re.findall(reg, s1)))
print(bool(re.findall(reg, s2)))

# 2я задача

s = 'В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных температур '
reg = r'[0-9]{2}/[0-9]{2}/[0-9]{4}'
print(re.findall(reg, s))
