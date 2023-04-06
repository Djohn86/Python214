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

# with open('data.csv') as f:
#     fn = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.reader(f, delimiter=';')
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году")
#         count += 1
#     print(f"Всего в файле {count} строки")

# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerow(['Name', 'Class', 'Age'])
#     writer.writerow(['Djohn', '9', '15'])
#     writer.writerow(['Ivan', '10', '15'])
#     writer.writerow(['Maxim', '11', '17'])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]

# with open('sw_data.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=';', lineterminator='\r')
#     writer.writerows(data)

# with open('sw_data.csv', 'w') as f:
#     name = ['Name', 'Age']
#     writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=None)
#     writer.writeheader()
#     writer.writerow({'name': 'Sasha', 'age': 8})
#     writer.writerow({'name': 'Sasha1', 'age': 8})
#     writer.writerow({'name': 'Sasha2', 'age': 6})
#     writer.writerow({'name': 'Sasha4', 'age': 7})
#     writer.writerow({'name': 'Sasha3', 'age': 18})


# Парсинг данных с сай

from bs4 import  BeautifulSoup


# f = open('index.html').read()
# soup = BeautifulSoup(f, 'html.parser')
# # row = soup.find_all('div', class_='row')[1].find(class_='name').text
# row = soup.find_all('div', {'data-set': 'salary'})
# print(row)

# import requests
#
# res = requests.get('https://ru.wordpress.org/')
# print(res.status_code)


# import requests
# from bs4 import BeautifulSoup
# import re
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# # def refined(s):
# #     return re.sub(r"\D+", "", s)
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     elements = soup.find_all('article', class_='plugin-card')
#     for el in elements:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ""
#
#         try:
#             url = el.find('h3').find('a').get('href')
#         except ValueError:
#             url = ""
#     print()
#
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/browser/blocks/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


from parse import Parser


def main():
    pars = Parser('https://www.ixbt.com/live/index/news/', 'news.txt')
    pars.get_html()
    pars.parsing()


if __name__ == '__main__':
    main()
