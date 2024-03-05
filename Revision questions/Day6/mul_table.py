# 2.Write a python program to display multiplication table of a number (user input)



number=int(input("enter the number"))

for num in range(1,11):
    print(f"{number}*{num}={number*num}")