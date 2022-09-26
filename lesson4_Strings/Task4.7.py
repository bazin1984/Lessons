print('..'.join(["a" , "b"]))      #   создает строку
print("1_2_3_4_5".split("_"))  # разбивает строку на список
from random import *
x = "1,2,3,4,5,6,7,8,9"
n = x[0::3]
print(n)
n = list(n)
shuffle(n)
psw = ''.join([choice(n) for y in range(5)])
print(psw)
print(type(psw))





