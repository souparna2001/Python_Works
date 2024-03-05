# Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, display
# “Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message”.

user=int(input("enter the message"))

if user==1 or 2 or 3:
  if user==1:
     print("Thank you")
  elif user==2:
     print("Well done")   
  elif user==3:
     print("Correct")   
  else:
     print("Error message")