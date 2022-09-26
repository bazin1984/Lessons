# 11. Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”].
# В новый список добавить элементы, которые содержат пробел.

s = ["hello my friend" , "my name is" , "house" , "cat" , "dog"]
with_whitespace = []
for i in s :
    if " " in i :
        with_whitespace.append(i)
print(with_whitespace)


     


