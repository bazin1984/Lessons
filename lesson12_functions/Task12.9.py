def is_prime(n) :
    d = 2
    while n % d != 0 :
        d += 1
    return n == d
print(is_prime(int(input("Введите число от 1 до 1000    "))))
