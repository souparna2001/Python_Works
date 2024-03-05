# Ask the user to enter their name and a number. If the number is less than 10, then display their name that number of times; otherwise display the message “Too high” 

name=input("enter the name : ")
num=int(input("enter the number : ")) 

if num<10:
  for i in range(num):
       print(name)
else:
       print("too high")       
              


              