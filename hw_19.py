# new_fail = open('work.txt', 'w')
# new_fail.write('Замена строки в файле;\nизменить строку в списке;\nзаписать список в файл;\n')
# new_fail.close()

# 1-е задание

# new_fail = open('work.txt')
# data = new_fail.readlines()
# print(data)
# data[1], data[2] = data[2], data[1]
# print(data)
# new_fail.close()
#
# new_fail = open('work.txt', 'w')
# new_fail.writelines(data)
# new_fail.close()

# 2-е задание

# new_fail = open('work.txt')
# data = new_fail.readlines()
# new_data = data[::-1]
# print(new_data)
# new_fail.close()
#
# new_fail = open('work.txt', 'w')
# new_fail.writelines(new_data)
# new_fail.close()

# 3-е задание

with open('work1.txt', 'w') as one, open('work2.txt', 'w') as two:
    one.write('Данные первого файла:\n -line 1\n -line 2\n -line 3\n')
    two.write('Данные второго файла:\n -line 4\n -line 5\n -line 6\n')

with open('work1.txt') as one, open('res.txt', 'w') as res, open('work2.txt', 'r') as two:
    for i in one:
        res.write(i)
    for j in two:
        res.write(j)


