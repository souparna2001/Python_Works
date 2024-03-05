# starting with 3 alphabet (uppercase)
# second place must be P,C,A,F,H or T           
# one alphabet(starting letter of name of the person)
# 4 digit
# one alphabet

from re import*

pan_card_format=input("enter the format")

rule="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(rule,pan_card_format)  

print("invalid" if matcher==None else "valid") 




