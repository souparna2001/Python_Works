num1=int(input("enter the number"))
num2=int(input("enter the number"))

print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n")

check=int(input("enter the selection"))

if (check==1):
    result=num1+num2
    print("ans is",result)
elif (check==2):
    result=num1-num2
    print("ans is",result) 
elif (check==3):
    result=num1*num2
    print("ans is",result)
elif (check==4):
    if (num2==0):
        print("division by zero is not possible")
    else:
       result=num1/num2
       print("ans is",result)   
else:
    print("you entered a wrong value")            