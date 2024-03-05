# 2.Write a python program that Take input from user and make square list of the number and the cube list .Range is 10 number in the list

# square_list=[]
# cube_list=[]
# count=0
# while True:
#   if count!=10:
#      number=int(input("enter the number="))
#      square=(number)**2
#      cube=(number)**3
#      square_list.append(square)
#      cube_list.append(cube)
#      count+=1
#   else:
#      break
# print(f"square of numbers:{square_list}") 
# print(f"cube of numbers:{cube_list}")



    



square_list=[]
cube_list=[]
for num in range(0,10):
  number=int(input("enter the number="))
  square=(number)**2
  cube=(number)**3
  square_list.append(square)
  cube_list.append(cube)
  
print(f"square of numbers:{square_list}") 
print(f"cube of numbers:{cube_list}")







