print("""Компьютер загадал число от 1 до 10 и цвет , красный/черный.
У Вас имеется 5 попыток чтобы отгадать и число и цвет.""")
from random import *
number = randint(1,10)
x = randint(1,2)
if x == 1 :
    colors = "красный"
else:
    colors = "черный"
print(number  ,  colors)
i = 0
u = 0
while u < 5 :
    u += 1
    a = int(input("Введите загаданное число  "))
    b = input("Введите загаданный компьютером цвет  ")
    if a == number and b == colors :
        print(f"Поздравляем, Вы отгадали и цвет и число с {u} попытки")
        i += 5
        break
    elif a != number and b == colors :
        print("Вы отгадали цвет, но не отгадали число")
        print(f"У Вас осталось {5 - u} попытки")
        break
    elif a == number and b != colors :
        print(f"Вы отгадали число, но не отгадали цвет , у Вас осталось {5 - u} попыток")
        b = input("Введите загаданный компьютером цвет")
        if b == colors :
            print(f"Вы отгадали и число и цвет с {u} попытки")
            i = 5
        break
    else:
        print(" Вы не отгадали ни число ни цвет")
        print(f"У Вас осталось {5 - u} попытки")
        if u > 5:
            i = 5
            break
while i < 5 - u :
    i += 1
    a = int(input("Введите загаданное компьютером число  "))
    if a > number :
        print("Ваше число больше загаданного")
        print(f"У Вас осталось {5 - i - u} попытки")
    elif a < number :
        print("Ваше число меньше загаданного")
        print(f"У Вас осталось {5 - i - u} попытки")
    else:
        print(f"Вы отгадали число с {i + u} попытки")
        break
else:
    print(f"У Вас закончились попытки, загаданное число = {number}  , цвет - {colors}")










































