lst=[2,3,4,5,6,7,8,9,10]
squares=[]

for num in lst:
    sq=num**2
    squares.append(sq)

# print(squares)    

# even=[]
# for num in lst:
#     if num%2==0:
#         even.append(num)

# print(f"even numbers in list are {even}")        


# cubes=[num**3 for num in lst]
# print(cubes)

# squares=[num**2 for num in lst]
# print(squares)

# even=[num for num in lst if num%2==0]
# print(even)

# odd=[num for num in lst if num%2!=0]
# print(odd)

num_gt_five=[num for num in lst if num>5]
print(num_gt_five) 

# c4=["manoj","bilal","akash","malavika","jamiya","akshy"]

# upper_names=[name.upper() for name in c4]
# print(upper_names)

# # print names whose length >4 
# name_gt_four=[name for name in c4 if len(name)>5]
# print(name_gt_four)

# lst=["red","green","blue","white","apple","ignore","under"]



# #[list comprehension]

#    # [# return value # for num in lst #condition]

# # vowels
# vowels=[word for word in lst if word.startswith(("a","e","i","o","u"))]
# print(vowels) 

# vowels=[word for word in lst if word[0] in (("a","e","i","o","u"))]
# print(vowels) 


# # consonants
# consonants=[word for word in lst if not word.startswith(("a","e","i","o","u"))]
# print(consonants) 

# consonants=[word for word in lst if not word[0] in (("a","e","i","o","u"))]
# print(consonants) 
