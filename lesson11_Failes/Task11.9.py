a = []
b = []
with open("333.txt" , "r") as file :
    s = file.readlines()
print(s)
for i in s :
    if i[-1] == "\n" :
        i = i[:-1]
    if i.isalpha() :
        i = str(i)
        a.append(i)
    elif i.isdigit() :
        i = int(i)
        b.append(i)
print(a)
print(b)


