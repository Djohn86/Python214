k = int(input("Введите количество копеек от 1 до 99: "))
if k % 10 == 1 and k != 11:
    print(k, "копейка")
elif 2 <= k % 10 <= 4 and not(12 <= k <= 14):
    print(k, "копейки")
else:
    print(k, "копеек")
