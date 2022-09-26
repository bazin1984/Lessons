# break - досрочно прерывает цикл
arr = [1, 2, 3, 4, 5]
for i in arr:
    print(i)
    if i == 4:
        break

for i in arr:
    if i == 4:
        break
    print(i)
