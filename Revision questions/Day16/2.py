# 2.Print the output in multiple row
#         Input: enter your name
#         Input: enter range 
#         Output: (print name up to the range)

name=input("enter the name : ")
g_range=int(input("enter the range : "))

if g_range>0:       
   for i in range(1,g_range+1):
      print(name)
elif g_range<0:
   print(f"enter range greater than 0")