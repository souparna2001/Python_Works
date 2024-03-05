from re import*

mobile_number=input("enter the no:") 

# rule="[+][9][1][0-9]{10}"

# or

rule="([+]91)?[0-9]{10}"

matcher=fullmatch(rule,mobile_number)

print("invalid" if matcher==None else "valid")