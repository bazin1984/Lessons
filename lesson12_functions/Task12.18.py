# Написать функцию, которая считает сколько гласных и согласных в строке. Строку вводить с клавиатуры.

def letters(s) :
    vowels = []
    consonant = []
    for i in s :
        if i.isalpha() :
            if i in ["a","o","i","e","u","y"] :
                vowels.append(i)
            else:
                consonant.append(i)
    return "Число гласных", len(vowels), "число соглаcных" , len(consonant)
s = input("Введите стороку   ").lower()
print(letters(s))




