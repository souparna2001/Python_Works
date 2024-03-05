from re import *

phone_number=input("enter the number")

rule="[+][0-9]{3}[0-9]{10}"

matcher=fullmatch(rule,phone_number)

print("invalid" if matcher==None else "valid")