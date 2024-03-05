# print all century years from starting year to current year

starting_year=int(input("enter the number"))

if starting_year%100==0: 

    while(starting_year<=2023):
        print(starting_year)
        starting_year+=100    




