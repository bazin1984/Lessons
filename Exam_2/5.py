# 5. Создайте словарь из строки ' An apple a day keeps the doctor away'    следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.

string_1 = ' An apple a day keeps the doctor away'
new_dictionary = {}
for keys in string_1:
    new_dictionary[keys] = new_dictionary.get(keys , 0) + 1
print(new_dictionary)

