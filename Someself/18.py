s = "abcdefghijklmnopqrstuvwxyz."
for i in range(6) :                
    print("-" * 38,end="\n")
    for l in s :
        if s.index(l) % 7 == i :
            print("| ", l.upper(),l , " |" , end=" ")
    print()
print("-" * 38)
