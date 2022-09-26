Month = {1:'jan' , 2:'feb',3:'mar',4:'apr',5:'may',6:'jun',7:'jul',8:'aug',9:'sep',10:'oct',11:'nov',12:'dec'}
count = len(Month)
print(count)

salary = {'direction' : 120800.0,
          'secretary' : 101150.25,
          'locksmith' : 188200.00}

print(salary)
del  salary['secretary']      # удаляем значение по ключу
print(salary)


for i in Month :                           # вывод через цикл
    print(i, ': ' , Month[i])


