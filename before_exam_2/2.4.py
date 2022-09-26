s = "Сидел барсук в своей норе и ел картошечку пюре"
print(len(s))
print(s + ".")
print("ре" in s)
print(s.count("ре"))
print(s[-2])
for i in s :
    if s.index(i) %2 != 0 :
        print(i,end=" ")
a = s.split()
print()
c = 0
for i in a :
    if len(i) > 1 :
        c += 1
print(c)
