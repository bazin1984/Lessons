with open("111" , "r+") as file :
    # file.write("hello 5 good 10 work_15 at _study 20 for me 25")
    l = file.readlines()
    print(l)
    k = 0
for i in l :
    i = i.replace("_" , " ")
    s = i.split(" ")
    print(i)
    print(s)
for i in s :
    if i.isdigit() :
        i = int(i)
        k += i
print(k)


