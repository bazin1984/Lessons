# вложенные словари

position = {'manager' : {'director','deputy director'},
            'teacher' : {'specialist', 'methodist','senior lecturer'},
            'staff' : {'cleaner','porter','watchman'}}
count1 = len(position)
count2 = len(position['manager'])
print(position,'len:' , count1, '\n', position['manager'], 'len :' , count2, '\n',
      position['staff'] )
a = list(position)
print(a)
print(position.keys())
for i in position :
    print(i)


