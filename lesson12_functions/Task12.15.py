#Написать функцию и сделать так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

def time(n) :
    s = n
    day = n // 86400
    n %= 86400
    hours = n // 3600
    n %= 3600
    min = n // 60
    sec = n % 60
    # return "дней",day,"часов",hours,"минут",min,"секунд",sec
# print(time(96020))
    print(f'''
{s} секунд это : 
    
Дней : {day}  часов : {hours}  минут : {min}   секунд : {sec}''')

n = 96500
time(n)


