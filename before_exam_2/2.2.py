s = [4,"you",1,"hello",9,"Ok",7,"Python",5]
numbers = []
letters = []
for i in s :
    if type(i) == int:
        numbers.append(i)
    else:
        letters.append(i)
a = sorted(numbers)
b = sorted(letters,key=len)
b.extend(a)
with open("1111.txt" , "w+") as file :
    for i in b :
        i = str(i)
        file.write(i)
        file.write(" ")
file = open("1111.txt" , "r")
print(*file)
file.close()
