# print all non century years from starting year to current year

starting_year=int(input("enter the year"))


while(starting_year<=2023):
           if starting_year%100!=0: 
               print(starting_year)
           starting_year+=1   


