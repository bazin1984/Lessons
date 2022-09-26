m = int(input("Введите целое число"))
n = int(input("Введите целое число"))
s = []
x = []
if m < n :
    for i in range(m,n+1) :
        s.append(i)
    print(s)
else:
    for i in range(n,m+1) :
        x.append(i)
    x.reverse()
    print(x)
