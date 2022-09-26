d_eng = {
    1 : ["a","e","i","o","u","l","n","s","t","r"],
    2 : ["d","g"],
    3 : ["b","c","m","p"],
    4 : ["f","h","v","w","y"],
    5 : ["k"],
    8 : ["j","x"],
    10 : ["q","z"]
}
d_rus = {
    1: ["а","в","е","и","н","о","р","с","т"],
    2 : ["д","к","л","м","п","у"],
    3 : ["б","г","ь","я"],
    4 : ["й","ы"],
    5 : ["ж","з","х","ц","ч"],
    8 : ["ш","э","ю"],
    10 : ["ф","щ","ъ"]
}
slovo = input().lower()
a = []
for i in slovo :
    l = 0
    while l < len(d_eng) :
        if i in d_eng[list(d_eng)[l]] :
            a.append(list(d_eng)[l])
        l += 1
for i in slovo :
    l = 0
    while l < len(d_rus) :
        if i in d_rus[list(d_rus)[l]] :
            a.append(list(d_rus)[l])
        l += 1
print(sum(a))





