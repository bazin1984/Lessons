# блок else выполняется , когда программа была завершена в нормальном режиме
for i in range(3) :
    if i == 10 :
        break
    print(i)
else:
    print("Готово")

i = 0
while i < 3 :
    print(i)
    i += 1
else:
    print("Готово")

