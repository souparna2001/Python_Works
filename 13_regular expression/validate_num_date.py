from re  import*

date=input("enter the date")

rule="(0?[1-9]|1[0-9]|2[0-9]|3[0-1])"
# rule=(0?[1-9]|[12][0-9]|3[0-1])"


matcher=fullmatch(rule,date)

print("invalid" if matcher==None else "valid")