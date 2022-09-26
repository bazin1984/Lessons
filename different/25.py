d = {
    "a" : 1,
    "b" : 2
}
s = "arty"
n = 0
for i in s :
    if i in d.keys() :
        n += d.get(i)
print(n)
        