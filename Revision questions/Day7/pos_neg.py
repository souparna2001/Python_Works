# 1. Write a Python program that separate positive and negative numbers from a list

numbers = [1, -2, 3, -4, 5, -6, 0]
positive_numbers = []
negative_numbers = []
non_negative_number=[]

for num in numbers:
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)
    elif num==0:
        non_negative_number.append(num)   


print(f"Given list {numbers}")
print(f"Positive numbers are {positive_numbers}")
print(f"negative numbers are {negative_numbers}")
print(f"non negative number are {non_negative_number}")




    