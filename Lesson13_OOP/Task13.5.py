# class Car :
#     def start(self):
#         print("Двигатель заведен")

# car_a = Car()
# print(car_a)          #  метод str выводит ячейку памяти для обьекта, можем перераспределить метод str

class Car :                 #  переопределим метод str
    def __str__(self):
        return "Car class Object"        # создание методов класса

car_a = Car()

print(car_a)




