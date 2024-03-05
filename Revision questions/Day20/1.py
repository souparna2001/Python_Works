# 1. Write a Python program to find the second largest number in a list.

lst=[28,16,46,19,10]

largest_num=0

for num in lst:
    if num>largest_num:
        second_largest=largest_num
        largest_num=num
    elif num>second_largest and num!=largest_num:
        second_largest=num
if second_largest==num:
    print("No second largest")
else:
    print("second largest num is:", second_largest)            


