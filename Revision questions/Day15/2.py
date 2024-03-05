# 2.Convert tuple to a list and find sum


elements=(5,8,10,2,20)

lst=list(elements)
result=0

for num in elements:
    result=result+num
print(f"tuple is {elements}")    
print(f"list is {lst} and their sum is {result}")  

