# 2.Write a python program to list the even numbers from the range that given by the user and delete the multiplication of 5 from the list


# User_input=int(input("enter the start number"))
# number=int(input("enter the end range"))
# for i in range(User_input,number):
#     if i%2==0 and i%5!=0:
#         print()

start=int(input("Enter starting range: "))
end=int(input("Enter ending range: "))

lst=[]
for i in range(start,end+1):
    if i %2==0:
        lst.append(i)
    
even_lst=[i for i in lst if i%5!=0]
print(even_lst)