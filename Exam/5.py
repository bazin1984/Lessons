m = int(input("Введите целое число"))
n = int(input("Введите целое число"))
if m < n :
    for i in range(m,n+1) :
        print(i,end=" ")
else:
    for i in range(m,n-1,-1) :
        print(i,end=" ")
