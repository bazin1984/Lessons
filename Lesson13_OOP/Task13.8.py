# Класс Human
# Создайте класс Human.
# Определите для него два статических поля: default_name и default_age.
# Создайте метод __init__(), который помимо self принимает еще два параметра: name и age.
# Для этих параметров задайте значения по умолчанию, используя свойства default_name и default_age.
# В методе __init__() определите четыре свойства: Публичные - name и age. Приватные - money и house.
# Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
# Реализуйте справочный статический метод default_info(), который будет выводить статические поля default_name и default_age.
# Реализуйте метод earn_money(), увеличивающий значение свойства money.



class Human :
    default_name = "Dima"
    default_age = 38

    def __init__(self,name=default_name,age=default_age):
        self.name = name
        self.age = age
        self.__money = 25
        self.__house = None

    def info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Money : {self.__money}")
        print(f"House : {self.__house}")

    @staticmethod
    def default_info():
        print(f"Default_name  :  {Human.default_name}")
        print(f"Default_age  :  {Human.default_age}")

    def earn_money(self,amount):
        self.__money += amount
        print(f"Earned {amount} money ! Current value : {self.__money}")


Human.default_info()    # вызываем статический метод

# dima = Human()
# dima.info()
#
# oleg = Human("Oleg",38)
# oleg.info()
#
# dima.earn_money(2500)
#
# dima.info()
# Human.default_info()