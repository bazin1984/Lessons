m = int(input("введите первое число"))
n = int(input("Введите второе число"))
if m <= n :
    for i in range(m,n+1) :
        print(i,end=" ")
else:
    print("Первое число должно быть меньше второго,  повторите ")

