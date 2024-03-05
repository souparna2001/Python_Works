#month 1-12


from re import*

month=input("enter the number of month")

rule="(0[1-9]|1[012])"

matcher=fullmatch(rule,month)

print("invalid" if matcher==None else "valid")