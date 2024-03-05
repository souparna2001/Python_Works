# 2.Write a python program to find the least square number from a list

lst1=[12,49,3,7,25,16]

lst2=[]

for num in lst1:
    sqr=int(num**0.5)
    lst2.append(sqr**2)
sort_lst=sorted(lst1)
sqr_roots=[num for num in lst1 if num in lst2]
least_sqrt=min(sqr_roots)  
print(f"list:{lst1}")
print(f"least squareroot in the list:{least_sqrt}")  




