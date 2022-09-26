while True:
    c = int(input("Введите 1 для начала работы , введите 0 для выхода"))
    if c == 0 :
        break
    elif c == 1 :
        x = float(input("Введите число x  "))
        s = input("Введите знак  + , - , * , /")
        y = float(input("Введите число y  "))
        if s == "+" :
            print(x + y)
        elif s == "-" :
            print(x - y)
        elif s == "*" :
            print(x * y)
        elif s == "/" :
            if y != 0 :
                print(x / y)
            else:
                print("Деление на ноль")




