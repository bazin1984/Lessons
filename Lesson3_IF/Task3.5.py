x = int(input("Введите первое число"))
y = int(input("Введите второе число"))
z = int(input("Введите третье число"))
if x - y > 0 and x - z > 0 :
    print("Число x наибольщшее")
elif y - x > 0 and y - z > 0 :
    print("Число y наибольшее")
else:
    print("Число z наибольшее")
