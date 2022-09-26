x = int(input("Ведите число  "))
y = int(input("Ведите число  "))
try :
    c = x / y
except ZeroDivisionError :
    print("деление на ноль ")
else:
    print( c ** 2 )
finally:
    print("Оператор finally выполнен")

