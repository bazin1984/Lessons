def function (N):
    if len(str(N))<4:
       summ =N + function(N*10)

       return summ
    else:
       return 0

print(function(1))