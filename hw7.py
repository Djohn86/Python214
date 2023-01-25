s = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]

pr = []
st = []
t = 0
for i in s:
    for j in range(1, i+1):
        if i % j == 0:
            t += 1
    if t == 2:
        pr.append(i)
        t = 0
    else:
        t = 0
        st.append(i)
print(pr)
print(st)


print("Максимальное значение среди чисел, не являющимися простыми: ", max(st))
print("Минимальное значение среди простых чисел: ", min(pr))
