# write a python program to reverse digits in a number

num=792001
rev=0
while(num!=0):
    last_digit=num%10
    rev=rev*10+last_digit
    num=num//10
print(rev)

