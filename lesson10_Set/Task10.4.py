num_set = {1,2,3,4,5,6}

num_set.update([8])
num_set.discard(3)        #  если элемента нет , то не выдаст ошибку
num_set.remove(1)        #   если элемента нет , то выдаст ошибку
print(num_set)
num_set.discard(8)
print(num_set)

print(num_set.pop())    # удаляет случайный элемент
print(num_set)

num_set.clear()
print(num_set)
