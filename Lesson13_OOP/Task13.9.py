# 2. Вы идете в путешествие, надо подсчитать сколько  денег у каждого студента. Класс студент описан следующим образом:
# Необходимо понять у кого больше всего денег и вернуть его имя. Если у студентов денег поровну вернуть: “all”.


class Student:
    def __init__(self, name, money):
        self.name = name
        self.money = money


student_1 = Student("Dima", 3000)
student_2 = Student("Sergei", 2000)
student_3 = Student("Oleg", 1800)
student_4 = Student("Pavel", 2200)
student_5 = Student("Anton", 1500)

students = [student_1, student_2, student_3, student_4, student_5]
moneys = []
for i in students:
    moneys.append(i.money)

if max(moneys) == min(moneys):
    print("all")
else:
    max_money = 0
    for i in students:
        if i.money > max_money:
            max_money = i.money
            name = i.name

    print(name, max_money)
