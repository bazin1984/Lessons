s = "##привет мир  вам"
print(s.strip('#'))
print(s.find('и',5,-1))

text = 'Never forget what you are, for surely the world will not'
print(f"Index Of N :{text.find('N')}\nIndex Of , : {text.find(',')}")

text = 'Never forget what you are, for surely the world will not'
print("Index Of N: " + str(text.find("N")) + "\n" + "Index Of ,: " +str( text.find(",")))

name = "Tirion"
print(name.replace("Ti","Ki").lower())