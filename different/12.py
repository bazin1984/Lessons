a = ["оценки",5,6,7,8,"школа",26,28,33,"город",312,444,555]
d = {}
s = None
for i in a :
    if type(i) == str :
        d[i] = []
        s = i
    else :
        d[s].append(i)
print(d)