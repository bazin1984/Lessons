s = "ячсМИтьбДЛРтимпНМАтьВЫАвррЫВПИ"  # Очистить от заглавных букв
s_new = " "
for i in s :
    if i.isupper() == False :
        s_new += i
print(s_new)