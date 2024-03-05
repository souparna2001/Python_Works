# 2) write a python program to find compound interest

# A=P(1+r/n)^nt    A=amount
# p=principle
# r=rate
# t=time 
# n=no.of times interst applied
 

P=int(input("enter the principle balance "))

r=int(input("enter the rate "))

n=int(input("enter the no.of times interest applied "))

t=int(input("enter the time "))

A=P*(1+r/n)**(n*t)
compound_interest=A-P

print(compound_interest)