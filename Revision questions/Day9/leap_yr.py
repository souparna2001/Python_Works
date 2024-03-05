# 1. Write a Python program to find leap year (user input)


year=int(input("enter the year: "))

if year%100==0 and year%400==0:
    print(f"{year} is a leap year")
elif year%100!=0 and year%4==0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")       