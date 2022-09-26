# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр.
# Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.

list = [15,48,'hello' , 6,19, 'world']
vowels = ['a','e','i','o','u','y']
number_of_vowels = []
number_of_consonants = []
for i in list :
    if type(i) == int :
        if i % 2 == 0 :
            a = [int(x) for x in str(i)]
            print(sum(a))
        else:
            a = list.index(i)
            list[a] = 1
    elif type(i) == str:
        for u in i:
            if u in vowels:
                number_of_vowels.append(u)
            else:
                number_of_consonants.append(u)
print(list)
print(f"количество гласных = {len(number_of_vowels)}")
print(f"количество согласных = {len(number_of_consonants)}")










