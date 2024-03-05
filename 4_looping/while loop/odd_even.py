start=1
end=int(input("enter the limit"))
   
while(start<=end):
    if start%2==0:
        print(f"{start} is even")
    else:
        print(f"{start} is odd")
    start+=1    