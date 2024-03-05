# list=[3,4,5,2,6,8,10]
# eg: sum=8 (3,5)
# eg: 7(4,3)(5,2)
# two_pair_sum

# list=[3,4,5,2]
# sum=int(input("enter the number "))
# list.sort()
# count=1
# for i in range(0,len(list)-1):
#     for j in range(i+1,len(list)):
#         cur_sum=list[i]+list[j]
#         if sum==cur_sum:
#             print(list[i],list[j])
#             break
#         count+=1

# print("loop count",count)


lst=[3,4,5,2]
sum=int(input("enter the sum "))

lst.sort()
low=0
upp=len(lst)-1
count=0

while(low<upp):
    curr_sum=lst[low]+lst[upp]

    if curr_sum==sum:
             print(lst[low],lst[upp])
             low+=1
             upp-=1
    elif curr_sum<sum: 
             low+=1
    elif curr_sum>sum:
             upp-=1 
    count+=1
print("loop counter",count)            
