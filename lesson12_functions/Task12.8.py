# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.

from random import *
def is_prime(number) :
    k = 0
    for i in range(2,number + 1) :
        if number % i == 0 :
            k += 1
    if k == 1:
        return True
    else:
        return False
number = randint(1,1001)
print(number)
print(is_prime(number))
