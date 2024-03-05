# 2. Ask the user to enter a number. If it is under 10, display the message “Too low”, if their number is 
#  between 10 and 20, display “Correct”, otherwise display “Too high”.  

user_enter=int(input("enter the number"))

if user_enter<10:
    print("too low")
# elif 10<=user_enter<=20:
elif user_enter>=10 and user_enter<=20:    
    print("correct")
else:
    print("too high")    