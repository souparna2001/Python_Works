# write a program to prirnt sum of even number in range

num1=int(input("enter the number"))
num2=int(input("enter the number"))

sum=0

for i in range(num1,num2+1):
    if i%2==0:
         sum=sum+i
print(sum)

# def sum_of_even_numbers(start, end):
#     sum_even = 0
    
#     for num in range(start, end + 1):
#         if num % 2 == 0:
#             sum_even += num
    
#     return sum_even

# # Example: Calculate and print the sum of even numbers in the range 1 to 10
# start_range = 1
# end_range = 10

# result = sum_of_even_numbers(start_range, end_range)

# print(f"The sum of even numbers in the range {start_range} to {end_range} is: {result}")



