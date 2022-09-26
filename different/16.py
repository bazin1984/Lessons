s = "1 2 3 4 5 6 4 5 7 2 1 3 6 8 7 1 9 0"
a= []
for i in s.split() :
    if i not in a :
        a.append(i)
        print("No")
    else:
        print("Yes")
