print('Введите правильный ответ на следующую задачу 3 + 4 - 7 = ?  , у Вас 5 попыток')
counter = 0
c = 3 + 4 - 7
while counter < 5 :
    counter += 1
    x = int(input("Введите число  "))
    if x > c :
        print(f"Ваше число больше, у Вас осталось {5 - counter} попыток ")
    elif x < c :
        print(f"Ваше число меньше, у Вас осталось {5 - counter} попыток")
    else:
        print(f"Вы ввели верный ответ с {counter} попытки")
        break
else:
    print(f"У Вас закончились попытки, верный ответ = {c}")

    