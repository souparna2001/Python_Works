s_year=int(input("enter the year"))
e_year=int(input("enter the year"))

for year in range(s_year,e_year+1): 
    if (year%100!=0 and year%4==0 or year%100==0 and year%400==0):
        print(year)

        
