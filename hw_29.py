import csv

with open('data2.csv') as f:
    dt = csv.reader(f, delimiter=';')
    i = 0
    for st in dt:
        if i == 0:
            n1 = st[0]
            n2 = st[1]
            n3 = st[2]
            n4 = st[3]
        else:
            print(f'{n1} - {st[0]}, {n2} - {st[1]}, {n3} - {st[2]}, {n4} - {st[3]}')
        i += 1




