product = lambda x,y : x * y    # анонимная функция lambda
print(product(2,5))
print(type(product))

def mul(a) :                          # вложенные функции
    def helper(b) :
        return a * b
    return helper
print(mul(2)(6))

