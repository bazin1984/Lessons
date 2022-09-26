s = [1,2,3,4,5,2,]
a = set(s)
if len(s) == len(a) :
    print("дубликатов нет")
else:
    print("дубликаты есть")
print(len(s) == len(a))