# (1-2)*(1-3)*.....*(1-n)  Составить программу вычисления выражения.

n = int(input("Введите число  "))
i = 2
s = 1
while i <= n :
    s *= (1 - i)
    i += 1
print(s)



