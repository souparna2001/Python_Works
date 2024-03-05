def leap (year):
    res="leap year" if year%100==0 and year%400==0 or year%100!=0 and year%4==0 else "not a leap year"
    return res
print(leap(2004))