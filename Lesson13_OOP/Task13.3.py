# Калькулятор.
# Создайте класс, где реализованы функции(методы) математических операций. А также функция, для ввод данных.

class Calc :
    def __init__(self):
        self.func4()

    def summ(self):
        return self.a + self.b

    def razn(self):
        return self.a - self.b

    def proizv(self):
        return self.a * self.b

    def delen(self):
        if self.b == 0 :
            return "error"
        return self.a / self.b

    def func4(self):
        self.a = int(input("number 1     "))
        self.b = int(input("number 2     "))

while True :
    x = input("Введите 0 для выхода , нажмите Enter для продолжения     ")
    if x == "0" :
        print("Это был простейший калькулятор, до свидания и до новых встреч!!!")
        break
    else:
        example = Calc()
        n = input("Введите знак + . / . - , * ")
        if n == "+" :
            print(example.summ())
        if n == "-" :
            print(example.razn())
        if n == "*" :
            print(example.proizv())
        if n == "/" :
            print(example.delen())
        if n not in ["/","*","-","+"] :
            print("Error")
