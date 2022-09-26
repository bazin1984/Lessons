s = "hello everybody , be happy"
s_2 = "HELLO EVERYBODY"
s_3 = "Hello Everybody"

print(s.title())  # делаем строку заголовком

print(s.replace("e",""))   # удаляет символ из строки(в ковычках пустое место, если что введем
print(s.replace("e","@"))                           # то заменит на этот символ
print(s.replace("e","A",2))   # заменяет символ указанное количество раз
print(s.replace("hello",""))  # удаляет слово из строки

print(s.translate({ord("e") : None}))   # заменяет каждый символ в строке( None - просто удаляет)
print(s.translate({ord(i): None for i in "elo" }))  # удаляет выбранные несколько символов


print(s.capitalize())  # делаем строку с заглавной буквы

print(s.upper())      # переводит строку в верхний регистр

print(s_2.lower())      # переводит строку в нижний регистр

print(s_3.swapcase())     # инверсия регистра

print(s.istitle())        # проверяет, являются ли строки заголовками.
print(s_2.istitle())
print(s_3.istitle())

s_4 = s.split(" ")
print(s_4)
print(s_4[0])
print(type(s_4))
