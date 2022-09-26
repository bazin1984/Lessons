# 7. Найти самое длинное слово в строке.
import re
string = "Интересно , какое тут самое длинное слово?"
new_list = re.split(r"\W+" , string)
del new_list[-1]
print(sorted(new_list,key=len)[-1])
