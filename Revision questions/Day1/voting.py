# Write a program to check whether a person is eligible for voting or not

age=int(input("enter the age"))

if age>=18:
    print("eligible to vote")
elif age<18:
    print("not eligible")    