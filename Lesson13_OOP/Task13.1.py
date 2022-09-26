class car :                     # создаем класс

    dafault_color = "grey"             #  статические поля(переменные класса)
    default_model = 5000


    def turn_on(self):          #  self  -  по умолчанию ссылка на параметр класса
        pass

    def ride(self):
        pass

    def __init__(self,color,model):        #   динамические поля (переменные обьекта)   self - привязкак к нашему классу

        self.color = color                        #  привязывает переменную color к классу
        self.model = model




car_object = car("красный" , 1000)     # создаем обьект в классе car

print(dir(car))                #  получаем список атрибутов класса( можно добавлять свои)




