months = set(["Jan","Feb","March","Apr","May","June","Jule","Aug","Sep","Oct",'Nov',"Dec"])
for i in months :
    print(i,end=" ")
print()
print("Apr" in months)

months.add("Year")
print(months)

months.update(range(1,13))
print(months)

months.update(["Месяц","Год","Неделя","День"])
print(months)