m = int(input("Введите целое число"))
n = int(input("Введите целое число"))
a = []
if m <= n :
    for i in range(m,n+1) :
        a.append(i)
    print(a)
else:
    print("Введите первое число меньшее второго")
