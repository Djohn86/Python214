import pickle

# file_name  = 'basket.txt'
#
# shop_list = {
#     'fruit': ['apple', 'mango'],
#     'ovoshi': 'carrot',
#     'deposit': 1000
# }
#
# with open(file_name, 'wb') as fh:
#     pickle.dump(shop_list, fh)
#
#
# with open(file_name, 'rb') as fh:
#     shop_list2 = pickle.load(fh)
#
# print(shop_list2)


# class Test:
#     num = 35
#     st = 'Hi'
#     lst = [1, 2, 3]
#     d = {'first': 'a', 'second': 2}
#     tpl = (22, 36)
#
#     def __str__(self):
#         return f'Number: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nСловарь: {Test.d}\nКортеж: {Test.tpl}'
#
#
# obj = Test()
#
# my_obj = pickle.dumps(obj)
# print(my_obj)
#
# new_obj = pickle.loads(my_obj)
# print(new_obj)

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __str__(self):
#         return f'{self.a} {self.b} {self.c(2)}'
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
#
# item = Test2()
# item2 = pickle.dumps(item)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)


import json

data = {
    'name': 'Olga',
    'age':  35,
    True: 1,
    'hobbies': ('running', 'singing'),
    'children':[
        {
            'firstname': 'Alice',
            'age': 6
        }
    ]
}

with open("date.json", 'w') as fw:
    json.dump(data, fw, indent=4)

with open("date.json", 'r') as fw:
    data1 = json.load(fw)

print(data1)

st = json.dumps(data)
print(st)

data2 = json.loads(st)
print(data2)