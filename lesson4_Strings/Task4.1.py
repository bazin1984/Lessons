m = 12345
x = str(m)
print(type(x))
print(x)

# Пример multi строки, внутри которой работают и ковычки и переносы :
x = '''Всем привет
давно хотел сказать
что я хочу обучаться )))'''
print(x)

a = "A"
b = "B"
text = f'''{a} и {b}    
сидели на трубе'''
print(text)

a = "Lannister, Targaryen, Baratheon, Stark, Tyrell..."
b = "they're all just spokes on a wheel."
c = "This one's on top, then that one's on top, and on and on it spins,"
d = "crushing those on the ground."
text = f'''{a}
{b}
{c}
{d}'''

print(text)


