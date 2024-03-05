s_year=int(input("enter the year"))
e_year=int(input("enter the year")) 

for year in range(s_year,e_year+1):

    if year%100!=0:
        print(year) 