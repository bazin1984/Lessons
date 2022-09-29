import sqlite3

# создаем базу данных
conn = sqlite3.connect("name1.db")
#создаем обьект cursor , который помогает нам взаимодействовать с БД и добавлять запись

cursor  = conn.cursor()

# создаем таблицу с двумя текстовыми колонками

#cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT , col_1 TEXT , col_2 TEXT) ''')

# заполняем таблицу данными

#cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ("Hello","world") ''')

# сохраняем изменения

#conn.commit()

#cursor.execute('''SELECT*FROM tab_1''')
#print(cursor.fetchall())        #  метод который выводит запрос из нашей таблички

#d = "red"      # добавляем данные в таблицу
#f = "black"

#cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?) ''' , (d,f))
#conn.commit()

# cursor.execute('''SELECT * FROM tab_1 ''')
# k = cursor.fetchall()
# print(k)

# удаление записи из таблицы по id , по значению

# cursor.execute(''' DELETE FROM tab_1 WHERE id = 2''')
# conn.commit()   #  сохраняем изменения
#
# cursor.execute(''' DELETE FROM tab_1 WHERE col_2 = "black" ''')
# conn.commit()
#
# cursor.execute('''SELECT*FROM tab_1''')
# print(cursor.fetchall())


# обновление данных в таблице

# t = 3
# n = "Wow"
# cursor.execute('''UPDATE tab_1 SET col_1 = ? WHERE id=?''' , (n ,t ))
# # cursor.execute(f'''UPDATE tab_1 SET col_1 = "PYTHON" WHERE id=6''')
# conn.commit()
#
# cursor.execute(''' SELECT * FROM tab_1''')
# k = cursor.fetchall()
# print(k)







