# print(1,2,3,4,5,sep=input())
# print(input(),"- Сказала она !")
# n = int(input())
# print(n%10,n//10%10,n//100%10)

# n = int(input())
# a_100 = n//100
# n = n%100
# a_20 = n//20
# n = n%20
# a_10 = n//10
# n = n%10
# a_5 = n//5
# n = n%5
# print(a_100,a_20,a_10,a_5,n)
# print(a_100+a_20+a_10+a_5+n)

# n = int(input())
# s = n // 1440 # количество суток
# m = n % 1440 # оставшиеся минуты после нахождения суток
# h = m // 60 # часы после нахождения суток
# m1 = m%60  # минуты оставшиеся после нахождения суток
# print(h,m1)

n = int(input())
sec_sut = n%86400
h_sut = sec_sut // 3600
sec_sut = sec_sut % 3600
min_sut = sec_sut // 60
sec_sut = sec_sut % 60
print(h_sut,":",min_sut//10,min_sut%10,":",sec_sut//10,sec_sut%10,sep="")
