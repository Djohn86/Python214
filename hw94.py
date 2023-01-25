def func(x):
    s = 0
    for i in x:
        s += i
        print(s, end=" ")
    print()


func([3, 9, 1])
func([2, 5, 4, 2])
func([3, 5, 10, 6, 3])

