# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
# # print(response.text)
# # print(todos)
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userID"]] += 1
#         except KeyError:
#             todos_by_user[todo["userID"]] = 1
#
# top_user = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_user)
#
# max_complete = top_user[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_user:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
# print(users)
# max_users = ' and '.join(users)
#
# s = 's' if len(users) > 1 else ''
# print(f'Users {max_users} comoleted {max_complete} TODOs')
#
# # print(' and '.join([]))
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo["userID"]) in users
#     return is_complete and has_max_count
#
#
# with open('filtr_data', 'w') as f:
#     filtered_todos = list(filter(keep, todos))
#     json.dump(filtered_todos, f, indent=2)

# import json
# data = {}
#
#
# class CoutryCapital:
#     def __init__(self, country, city):
#         self.country = country
#         self.city = city
#         data[self.country] = self.city
#
#     def __str__(self):
#         return f"{self.country}: {self.city}"
#
#     @staticmethod
#     def add_country(file_name):
#         new_country = input('Введите название страны: ')
#         new_city = input('Введите название столицы: ')
#         try:
#             data1 = json.load(open(file_name))
#         except ModuleNotFoundError:
#             data1 = {}
#
#         data1[new_country] = new_city
#
#         with open(file_name, 'w') as f:
#             json.dump(data1, f, indent=2, ensure_ascii=False)
#
#
# file = 'list_capital.json'
# index = 0
# while index <= 6:
#     try:
#         index = int(input('Выбор действия:\n1 - добавление данных'
#                           '\n2 - удаление данных'
#                           '\n3 - поиск данных'
#                           '\n4 - редактирование данных'
#                           '\n5 - просмотр данных'
#                           '\n6 - завершение работы'
#                           '\n'))
#         if index == 1:
#             CoutryCapital.add_country(file)
#
#         if index == 5:
#             CoutryCapital
#     except IndexError:
#         break

import csv

with open('data.csv') as f:
    file_reader = csv.reader(f, delimiter=';')
    count = 0
    for row in file_reader:
        if count == 0:
            print(f"Файл содержит столбцы: {', '.join(row)}")
        else:
            print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году")
        count += 1
    print(f"Всего в файле {count} строки")
