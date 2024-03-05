# .Write a program to print table of a number accepted by user. 

number=int(input("enter the number"))

for num in range(1,11):
    mul_table=number*num
    print(f"{num}*{number}={mul_table}")
    