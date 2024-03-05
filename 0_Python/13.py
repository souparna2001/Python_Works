# . Ask the user to enter 5 numbers and find the average using for or while loop

total=0
for i in range(5):
    num=int(input("enter the num"))
    total+=num
average=total//5  
print(average)

