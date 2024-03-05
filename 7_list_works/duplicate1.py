arr=[4,9,5,6,9,5,4,8,10,11,12]
arr.sort()
i=0
count=1

while(i<len(arr)-1):
    j=i+1
    i_element=arr[i]
    j_element=arr[j]   
    diff=j_element-i_element

    if diff==0:
        print(i_element)
        i=j
    count+=1     
    i+=1

print(f"count is {count}")