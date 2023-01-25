d = {'emp1': {'name': 'John', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}}

print(d['emp3'])

d['emp3']['salary'] = int(input("Введите зарплату: "))

for i in d:
    print(i)
    for j in d[i]:
        print(j, ':', d[i][j])
