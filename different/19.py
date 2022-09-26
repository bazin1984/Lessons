s = "adhfaf   5465498  #$%&*(&%$#@ sfgher hgsgrgrtw"
a = [0] *26
for i in s :
    if i >= "a" and i <= "z" :
        n = ord(i) -97
        a[n] += 1
for i in range(26) :
    print(chr(i +97) , a[i] , end=" ")
