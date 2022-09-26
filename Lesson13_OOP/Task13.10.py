# 1. Реализовать калькулятор с 4 методами: Сумма, вычитание , умножение, деление.
# Метод принимает 2 аргумента и возвращает результат.
# Невалидные данные должны быть обработаны

class Calc:

    # функция для проверки на валидность
    def valdate_numbers(self,first_number,socond_number):
        is_valid_first_number = isinstance(first_number,int) or isinstance(first_number,float)
        is_valid_second_number = isinstance(socond_number,int) or isinstance(socond_number,float)
        if is_valid_first_number and is_valid_second_number:
            print("Valid")
        else:
            raise Exception("Not Valid")

    def summ(self,first_number,second_number) :
        self.valdate_numbers(first_number,second_number)
        sum = first_number + second_number
        return sum

    def different(self,first_number,second_number):
        self.valdate_numbers(first_number, second_number)
        diff = first_number - second_number
        return diff

    def multiplication(self,first_number,second_number):
        self.valdate_numbers(first_number, second_number)
        multi = first_number * second_number
        return multi

    def division(self,first_number,second_number):
        self.valdate_numbers(first_number, second_number)
        if second_number == 0 :
            print("ERROR")
        else:
            div = first_number / second_number
            print(div)
            return div


my_culc = Calc()

print(my_culc.multiplication(4,2))






