# import json
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ''
#         for i in self.marks:
#             a += str(i) + ', '
#         return f'Студент: {self.name}: {a[:-2]}'
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def del_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def avereng_mark(self):
#         return round(sum(self.marks)/len(self.marks), 2)
#
#     def dump_to_json(self, filename):
#         data = {'name': self.name, 'marks': self.marks}
#         with open(filename, 'w') as f:
#             json.dump(data, f)
#
#     def load_from_file(self, filename):
#         with open(filename) in f:
#
#
#
#
#
# class Group:
#     def __init__(self, students):
#         self.students = students
#
#     def __str__(self):
#         a = ', '.join(map(str, self.students))
#         return f'\n{a}\n'
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         self.students.pop(index)
#
#     @staticmethod
#     def change_group(group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#
# st1 = Student('Vasiliy', [5, 4, 3, 4, 5, 3])
# st2 = Student('Djohn', [5, 4, 5, 5, 5, 3])
# st3 = Student('K', [5, 3, 5, 2, 5, 3])
# sts = [st1, st2]
# st1.dump_to_json('student_json')
# print(st1)
# st1.add_mark(4)
# print(st1)
# st1.del_mark(3)
# print(st1)
# st1.edit_mark(2, 5)
# print(st1)
# print(st1.avereng_mark())
# my_group = Group(sts)
# print(my_group)

import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
# print(response.text)
print(todos)
