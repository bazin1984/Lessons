list = [1,2,3,4,5,6,7,8,9]
print(list)
def change(list) :
    first_remove = list.pop()
    second_remove = list.pop(0)
    list.append(second_remove)
    list.insert(0,first_remove)
    return list
print(change(list))
print(list)

def change(list) :
    list[0] , list[-1] = list[-1] , list[0]
    return list
print(change(list))