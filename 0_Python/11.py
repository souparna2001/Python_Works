# Ask how many people the user wants to invite to a party.
#  If they enter a number below 10, ask for the names and 
# after each name display “[name] has been invited”.               
# If they  enter a number which is 10 or higher, display the message “Too many people”. 

no_people=int(input("enter the number"))  

if no_people<10:
    for i in range(no_people):
       name=input(f"enter the name of the people {i+1}:")
       print(f"{name} has been invited")
else:
    print("too many people") 

     
# {} values should be inserted.
# i+1: This expression calculates the value of i+1.
# So, when you see f"Enter the name of the person {i+1}:",
# it means that the value of i+1 will be inserted into the string. 
# For example, if i is 0 in the first iteration,
#  it becomes f"Enter the name of the person {0+1}:", 
#  which is equivalent to "Enter the name of the person 1:".

