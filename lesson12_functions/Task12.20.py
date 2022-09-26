# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.


def func(s) :
    if type(s) == tuple :
        n = 0
        for i in s :
            if type(i) is str:
                n += len(i)
        return n
    if type(s) == list :
        number = 0
        letters = 0
        for i in s :
            if type(i) == int :
                number += 1
            else:
                for u in i :
                    letters += 1
        return number , letters
    if type(s) == int :
        a = [int(i) for i in str(s)]
        n = 0
        for i in a :
            if i %2 != 0 :
                n += 1
        return n
    if type(s) == str :
        letters = 0
        for i in s :
            if i.isalpha() :
                letters += 1
        return letters

print(func(("Dima","Zadvorny",38,"years")))
print(func(["Python",5,15,25,35,"Java"]))
print(func(254168))
print(func("Hello everybody , '25',' 45', '78', '98' , bye bye!"))













