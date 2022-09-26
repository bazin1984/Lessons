i = 0
s = 0
n = 0
while i < 5 :
    i += 1
    x = int(input("Введите число  "))
    if x > n :
        s += 1
    n += x
if s == 5 :
    print("Возрастает")
else:
    print("Не возрастает")

