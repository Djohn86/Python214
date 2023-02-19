# f = open('fail.txt', 'a')
# lines = ['\nline 1', '\nline 2']
# f.writelines(lines)
# f.close()


# f = open('fail.txt', 'w')
# lst = [str(i**5) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()


# my_file = open('text1.txt', 'w')
# my_file.write('Заменить строку в текстовом файле;\nизменить строку в списке; \nзаписать список в файл;')
# my_file.close()
#
# my_file = open('text1.txt', 'r')
# read_file = my_file.readlines()
# print(read_file)
# read_file[1] = 'Hello world\n'
# my_file.close()
#
# my_file = open('text1.txt', 'w')
# my_file.writelines(read_file)
# my_file.close()

# f = open('text.txt', 'r')
# # print(f.read(3))
# # print(f.tell())
# print(f.seek(1))
# print(f.read())
# f.close()


# f = open('text.txt', 'w+')
# print(f.write('Я изучаю Питон'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
#
# f.close()


# file_name = 'res.txt'
# lst = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
#
# with open(file_name, 'w+') as my_file:
#     my_file.write('\t'.join(map(str, lst)))

# def longest_world(file):
#     with open(file, 'r') as test:
#         w = test.read().split()
#         max_len = len(max(w, key=len))
#         print(max_len)
#         print(w)
#         res = [word for word in w if len(word) == max_len]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_world('test.txt'))


# text = 'text N1\ntext N2\ntext N3\ntext N4\ntext N5\ntext N6\ntext N7\ntext N8\ntext N9\ntext N10\n'
# with open('one.txt', 'w') as f:
#     f.write(text)
#
# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("text", "Линия - ")
#         fw.write(line)

import os

# print(os.getcwd())
# print(os.listdir())
# print(os.listdir('../..'))
# os.mkdir('folder')
# os.makedirs('mast1/mast2/mast3')
# os.remove('test.txt')
# os.rmdir('folder')
# os.rename('mast1', 'global')
# os.rename('two.txt', 'global/test.txt')

for root, dir, files in os.walk('global'):
    print('root', root)
    print('dir', dir)
    print('files', files)


