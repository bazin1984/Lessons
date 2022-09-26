def freq(string, substring)  :
    return round((string.count(substring) / len(string)) * 100, 2)
print(freq("я хочу учиться ,учиться ,  хочу, учиться, учиться" , "учиться"))

