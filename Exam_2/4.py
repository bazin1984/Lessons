# 4. Создайте 2 множества:
# - Если они одинаковые: вывести что они равны
# - Если 1 множество полностью состоит из второго: вывести сообщение множество 1
# состоит из множества2
#
# - Если 2 множество полностью состоит из 1: вывести сообщение множество 2
#  	 состоит из множества 1
#
# - Если они пересекаются: вывести элементы в которых они пересекаются
# - Если не пересекаются: вывести сообщение об этом

set_1 = {1,2,3,4,5}
set_2 = {1,2,3}
if set_1 == set_2 :
    print('Множества равны')
else:
    print("Множества не равны")
if set_1 > set_2 :
    print("множество 2 является подмножеством 1")
elif set_2 > set_1:
    print("множество 2 является подмножеством 1")
if set_1 & set_2 :
    print(set_1 & set_2)
else:
    print("Множества не пересекаются")