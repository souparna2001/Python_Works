# . Write a Python program that ask users to enter a number and keep asking the users to enter a correct number, 
#  until the number with in the range that we given


num=int(input("enter the number"))

if num in range(20,30):
    print("entered number is in the range mentioned")
else:
    print("the number is not in the range mentioned")
    num=int(input("enter the number:"))
    for i in range(0,10):
        if num in range(20,30):
            print("entered numberr is in the range mentioned")
            break
        else:
            print("entered number is not in the range mentioned")
            num=int(input("enter another number"))