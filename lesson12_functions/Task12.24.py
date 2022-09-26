# s = ["aaa",["aaa","aaa",["aaa","aaa"],"aaa","aaa"],"aaa","aaa","aaa"]
# def summ(s) :
#     n = 0
#     for i in s :
#         if type(i) is not list :
#             for u in i :
#                 n += 1
#         else:
#             n += summ(i)
#     return n
#
# print(summ(s))


s = [1,2,3,[4,5,6],7,8,9]
def f(s) :
    n = 0
    for i in s :
        if type(i) is not list :
            n += i
        else:
            n += f(i)
    return n

print(f(s))

