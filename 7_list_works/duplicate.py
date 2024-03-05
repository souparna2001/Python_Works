# find duplicate numbers
arr=[4,9,5,6,9,5,4] 

arr.sort
count=1

for i in range(0,len(arr)-1):
    for j in range(i+1):
        ith_element=arr[i]
        jth_element=arr[j]
        diff=jth_element-ith_element
        if diff==0:
            print(ith_element)
            break
        count+=1

print(f"count={count}")

