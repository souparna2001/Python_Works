# Write a python program to display Fibonacci series and specify that number odd or even


prev=0
current=1
for i in range(0,15):
        next=prev+current
        print(prev,end=" is ")
        number="even" if prev%2==0 else "odd"
        print(number)
        prev=current
        current=next


