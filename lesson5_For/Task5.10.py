# Дан массив чисел,найти сумму чисел и произведение.
x = [1,3,5,7,9,2,4,6,8]
sum = 0
pr = 1
for i in x :
    sum += i
    pr *= i
print("Сумма чисел = " , sum)
print("Произведение чисел = " , pr)