a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
c = int(input("Введите третье число"))
if a > b and a > c:
    print("Наибольшее", "a")
else:
    if b > c:  # вложенный оператор
        print("Наибольшее", "b")
    else:
        print("Наибольшее", "c")
