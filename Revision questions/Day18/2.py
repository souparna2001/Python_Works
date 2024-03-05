# 2.	Write a program to calculate the electricity bill. Accept the number of units consumed from the user
# Unit                        Price
# First 100 units       No charge
# Next 100 units        Rs 5 per unit
# After 200 units       Rs 10 per unit
# For example if input unit is 350 then total bill amount is Rs 2000
users = int(input("Enter the number of users: "))

for user in range(2):
    units_consumed = int(input(f"Enter the number of units consumed for User {user}: "))
    if units_consumed <= 100:
        charge= 0
    elif units_consumed <= 200:
        charge = (units_consumed - 100) * 5
    else:     
       charge = 100 * 5 + (units_consumed - 200) * 10
    print(f"electricity bill for User {user} is {charge}")
    
    
    
    
   
        
        
    



