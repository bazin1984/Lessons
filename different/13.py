s = "hjfjhff uihkhkg dtdrrty"
d = {}
for i in s :
    if i.isalpha() == True :
        d[i] = d.get(i,0) + 1
print(d)
