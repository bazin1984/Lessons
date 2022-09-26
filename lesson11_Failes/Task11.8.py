words = []
numbers = []
with open("222" , "r+") as file :
    # file.write("9\naaa\n5\na\n2\naaaaa\n6\naa\n1")
    s = file.readlines()
print(s)
# a = [i.strip() for i in s]
# print(a)
# for i in a :
#     if i.isdigit() :
#         numbers.append(i)
#     else:
#         words.append(i)
# print(sorted(numbers) + sorted(words))


for i in s :
    if i[-1] == "\n" :
        i = i[:-1]
    if i.isdigit() :
        numbers.append(i)
    elif i.isalpha() :
        words.append(i)
print(words)
print(numbers)