# Массив из 7 цифр. Если четных цифр в нем больше чем нечетных,
# то найти сумму всех его цифр, если нечетных больше, то найти произведение 1 3 и 6 элемента.
from random import *
mas = [randint(1,99) for i in range(7)]
print(mas)
en_even_number = []
odd_number = []
s = 0
for numbers in mas :
    if numbers %2 == 0 :
        en_even_number.append(numbers)
    else:
        odd_number.append(numbers)
print(en_even_number)
print(odd_number)
if len(en_even_number) > len(odd_number) :
    for numbers in mas :
        s += numbers
    print("Сумма равна = " ,s)
else:
    print("Произведение равно =  " , mas[0] * mas[2] * mas[5])
