try :
    num_1 = int(input("Введите число  "))
    num_2 = int(input("Введите число  "))
    result = num_1 / num_2
except ZeroDivisionError :
    print("Деление на ноль")
except ValueError :
    print("Ошибка ввода переменной")
except Exception :
    print("Другая ошибка")
else:
    print("Ошибок не обнаружено")
    print(result)
finally:
    print("The end")

