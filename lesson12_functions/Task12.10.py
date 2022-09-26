from random import *
def sr_arif(mas) :
    return sum(mas)/len(mas)
mas = [randint(0,100) for i in range(10)]
print(mas)
print(sr_arif(mas))
