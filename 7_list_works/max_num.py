# convert number to string

nums=[12,67,5,8]
str_nums=[str(n) for n in nums]
print(str_nums)


# convert string to descending order(9-1) 
# checking numbers one by one

nums=[12,67,5,8]      #result is like 8,67,5,12
str_nums=[str(n) for n in nums]
str_nums.sort(reverse=True)              
print(str_nums)
