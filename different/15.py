# n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому
# школьнику? Сколько яблок останется в корзинке? Программа получает
# на вход числа n и k и должна вывести искомое количество яблок (два числа).

n = int(input("Введите количество школьников   "))
k = int(input("Введите количество яблок    "))
oststok = k % n
dostatok = k // n
print(f''' достанется каждому - {k//n} яблок 
останется в корзине - {oststok}  яблок''')

