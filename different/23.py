import re
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
def isCyrilic(slovo) :
    return bool(re.search("[а-я,А-Я]" , slovo))
slovo = input("Input words    ").lower()
if isCyrilic(slovo) :
    print(sum([k for letter in slovo for k , v in d_rus.items() if letter in v ]))
else:
    print(sum([k for letter in slovo for k , v in d_eng.items() if letter in v]))








