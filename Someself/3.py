# Проверить , является ли число простым.Если не простое ,то вывести все делители.
x = int(input("Введите число"))
k = 0  # Ввели делитель числа
delit = []
for i in range(1, x + 1):   # С помощью цикла перебираем и провряем на делители
   if x % i == 0 :
       k += 1
       delit.append(i)      # выводим делители не простого числа
if k == 2 :
    print("Число простое")
else:
    print("Число не простое")
    print(delit)

