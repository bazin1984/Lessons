# дано 15 целых и дробных чисел,  посчитать количество целых чисел
i = 1
s = 0
while i <= 15 :
    a = float(input("Введите число  "))
    if a % 1 == 0 :
        s += 1
    i += 1
print(s)