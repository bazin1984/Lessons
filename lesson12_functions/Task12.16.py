#Функцию которая при заданном целом числе n посчитает n + nn + nnn.

# def func(n) :
#     s = [str(n)*i for i in range(1,4) ]
#     summ = 0
#     for i in s :
#         summ += int(i)
#     print(*s , " сумма чисел = " , summ)
# func(5)

def func(n,i = 1) :
    if i > 3:
        return ""
    while i <=  3 :
        a = str(n) * i +" " + str(func(n, i + 1))
        return a

print(func(3))