# 1. Write a python program to create a list of tuples having first element as the number and second element as the cube of the number

lst=[]
for num in range(0,5):
    number=int(input("enter the number :"))
    lst.append((num,num**3))
print(lst)
    


 
