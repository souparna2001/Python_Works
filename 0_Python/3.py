# 3. Ask the user’s age. If they are 18 or over, display the message “You can vote”, if they are aged 17, disp
#  lay the message “You can learn to drive”, if they are 16, display the message“You can  buy a lottery ticket”,
# if they are under 16, display the message “You can go for treat”.


age=int(input("enter the age"))

if age>=18:
    print("you can vote")
elif age==17:
    print("yoy can learn to drive")
elif age==16:
    print("you can buy a lottery ticket")
elif age<16:
    print("you can go for treat")




       