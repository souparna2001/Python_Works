# Write a program to find the largest number out of three numbers excepted from user.

num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))

if num1>num2 and num1>num3:
    print(f"{num1} is the largest")
elif num2>num1 and num2>num3:
    print(f"{num2} is the largest")  
elif num3>num1 and num3>num2:
    print(f"{num3} is the largest") 
else:
    print("3 numbers are equal" )     


