import re

s1 = '+7 499 456-45-78'
s2 = '+74994564578'
s3 = '7 (499) 456 45 78'
s4 = '7 (499) 456-45-78'
s5 = '8 922 45236 54'


def val_tel(m):
    # reg = r'[+]?7[\s]?[(]?[4-9]{3}[)]?[\s]?[0-9]{3}[\s]?[-]?[0-9]{2}[\s]?[-]?[0-9]{2}'
    reg = r'[+]?[7-8][\s]?[(]?[\d]{3}[)]?[\s]?[\d]{3}[\s]?[-]?[\d]{2}[\s]?[-]?[\d]{2}'
    return re.findall(reg, m)


print(val_tel(s1))
print(val_tel(s2))
print(val_tel(s3))
print(val_tel(s4))
print(val_tel(s5))
