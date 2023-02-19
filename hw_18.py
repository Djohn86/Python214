a = [5, 9, 6, 7]
b = [3, 11, 8]
c = [2, 4]
d = [10, 1, 12]

new_list = a + b + c + d


def shell_up(x):
    red_line = len(x)
    while red_line > 0:
        for i in range(red_line, len(x)):
            vol_a = x[i]
            ind = i
            while ind >= red_line and x[ind - red_line] > vol_a:
                x[ind] = x[ind - red_line]
                ind -= red_line
                x[ind] = vol_a
        red_line //= 2
    return x


def merge_down(x):
    n = len(x)
    if n < 2:
        return x

    left = merge_down(x[:n // 2])
    right = merge_down((x[n // 2: n]))
    i = j = 0
    res = []

    while i < len(left) or j < len(right):
        if not i < len(left):
            res.append(right[j])
            j += 1
        elif not j < len(right):
            res.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res.append(right[j])
            j += 1
        else:
            res.append(left[i])
            i += 1
    return res


def search(x, item):
    m = False
    ind = 0
    while ind < len(x) and not m:
        if x[ind] == item:
            m = True
        else:
            ind += 1

    return m


print(new_list)

print('1 - сортировка по убыванию')
print('2 - сортировка по возрастанию')
menu = input('Выберите сортировку: ')
if menu == '1':
    print(merge_down(new_list))
elif menu == '2':
    print(shell_up(new_list))

lok = int(input("Введите значение для поиска: "))
if search(new_list, lok):
    print('Значение', lok, "найдено")
else:
    print("введенное значение не найдено")
