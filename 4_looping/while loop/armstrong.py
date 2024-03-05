num=input("enter the number")
digit_count=len(num)
num=int(num)
n=num
sum=0
 
while(num!=0):
    last_digit=num%10
    exp=last_digit**digit_count
    sum=sum+exp
    num=num//10

print(sum)
print("armstrong" if n==sum else "not armstrong")    














