a = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
b = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
if sum(a) > sum(b):
    print("Сумма больше в картеже a")
else:
    print("Сумма больше в картеже b")

print(a.index(min(a)),"\n", +b.index(min(b)))