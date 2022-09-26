# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.


class Example() :
    def __init__(self) :
        self.s = input("Введите данные     ")

    def func_1(self):
        if self.s.isdigit()  is True :
            n = 0
            for i in self.s :
                if int(i)%2 == 0 :
                    n += int(i)
            return len(self.s) * n
        else:
            vowels = ["a","o","i","u","y","e"]
            n_1 = 0
            n_2 = 0
            a = []
            b = []
            for i in self.s :
                if i in vowels :
                    a.append(i)
                    n_1 += 1
                else:
                    b.append(i)
                    n_2 += 1
            if n_1 * n_2 <= len(self.s) :
                return a
            else:
                return b

for_example = Example()
# print(for_example.func_1())

print(Example.func_1(for_example))






