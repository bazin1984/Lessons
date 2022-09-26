x = int(input("Ведите число  "))
i = 1
k = 0
s =[]
while i <= x :
    if x % i == 0 :
        k += 1
        s.append(i)
    i += 1
if k == 2 :
    print("Число простое")
else:
    print("Число составное")
    print(s)