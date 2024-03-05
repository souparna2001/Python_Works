# 2.Write a python program to accept decimal number and display it’s binary number


num=int(input("enter the number:"))

binary=0
value=1

while num>0:
    rem=num%2
    binary=binary+rem*value
    value=value*10
    num=num//2
print(f"binary of decimal number{num} is:{binary}")    