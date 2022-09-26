#  Словари

d = {}
c = {'dict' : 1, 'dictionary' : 2}
print(c)

a = dict(short='dict' , long='dictionary')    # метод создания словаря
a_1 = dict([(1,1) , (2,4)])           # ключ - значение, ключ - значение
print(a, "\n", a_1)

e = dict.fromkeys(['a' , 'b'])
e_1 = dict.fromkeys(['a' , 'b'] , 100)
print(e, '\n' , e_1)

f = {a : a ** 2 for a in range(7)}      # генератор словарей
print(f)


