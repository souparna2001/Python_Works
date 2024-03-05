# 1. Write a Python program that accepts a string and calculates the number of digits and letters.

string_accept=input("enter the string ")

letters=0
digits=0

for ch in string_accept:
    if(ch.isalpha()):
        letters+=1
    elif(ch.isdigit()):
        digits+=1

print(f"number of letters {letters}")
print(f"number of digits {digits}")




















