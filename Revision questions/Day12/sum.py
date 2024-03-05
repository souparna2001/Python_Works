# 1. Write a Python program that keep on accepting number from the user until users enter zero display the sum of all number


sum=0

while True:
      n=int(input("enter the number"))
      if n!=0:
            sum=sum+n
      else:
            break
      
print(sum)            