try :
    n_1 = int(input("введите первое число  "))
    n_2 = int(input("введите второе число  "))
    result = n_1 / n_2
except ValueError :
    print("Ошибка ввода , ведите числа   ")
    n_1 = int(input("введите первое число  "))
    n_2 = int(input("введите второе число  "))
    try :
        n_1 / n_2
    except ZeroDivisionError :
        print("ошибка деления на ноль")
        print("Введите числа")
        n_1 = int(input("Введите число"))
        n_2 = int(input("Введите число"))
        print(n_1 / n_2)
    else:
        print(n_1 / n_2)
except ZeroDivisionError :
    print("Ошибка - деление на ноль, повторите ввод")
    n_1 = int(input("Введите первое число   "))
    n_2 = int(input("введите второе число  "))
    print(n_1 / n_2)
else:
    print(result)








