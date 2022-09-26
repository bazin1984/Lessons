def season(mounth) :
    if 1<=mounth<=2 or mounth==12:
        return "Зима"
    elif 3<=mounth<=5 :
        return "Весна"
    elif 6<=mounth<=8 :
        return "Лето"
    elif 9<=mounth<=11 :
        return "Осень"
print(season(int(input("Введите номер месяца    "))))