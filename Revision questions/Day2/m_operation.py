num1=int(input("enter the first number "))
num2=int(input("enter the second number ")) 

selected_operator=int(input("press 1)addition 2)substraction 3)multiplication 4)division 5)exponent 6)modulus 7)floor division"))
print(selected_operator)

if selected_operator==1:
        addition=num1+num2
        print(f"addition answer is {addition}")

elif selected_operator==2:
        sub_result=num1-num2
        print(f"substraction answer is {sub_result}")

elif selected_operator==3:
       mul_result=num1*num2
       print(f"multiplication is {mul_result}") 

elif selected_operator==4:
        div_result=num1/num2
        print(f"division is {div_result}")  

elif selected_operator==5:
        exp_result=num1**num2
        print(f"exponent is {exp_result}") 

elif selected_operator==6:
        mod_result=num1%num2
        print(f"modulus answer is {mod_result}")   

elif selected_operator==7:
        floor_result=num1//num2
        print(f"floor division is {floor_result}")        





