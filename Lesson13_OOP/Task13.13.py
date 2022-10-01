# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.

class Example :

    def func(self,s):
        a = []
        if s.isdigit():
            for i in str(s) :
                i = int(i)
                if i % 2 == 0 :
                    a.append(i)
            return sum(a) * self.lens(s)
        elif s.isalpha():
            s_gl = 0
            s_sogl = 0
            gl = []
            sogl = []
            d = ["e","u","i","o","a","y"]
            for i in s :
                if i in d :
                    s_gl += 1
                    gl.append(i)
                else:
                    s_sogl += 1
                    sogl.append(i)
            if s_gl * s_sogl <= self.lens(s) :
                return gl
            else:
                return sogl

    def lens(self,s):
        return  len(str(s))

example = Example()
s = input("Введите   ")
print(example.func(s))





