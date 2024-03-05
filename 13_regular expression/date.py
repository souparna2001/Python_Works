from re import*

date=input("enter the date")
rule="(0?[1-9]|1[0-9]|2[0-9]|3[0-1])-(0?[1-9]|1[012])-(19[0-9]{2}|20[0-9]{2})"
    #    "(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[012]-((19|20)[0-9]{2})"

matcher=fullmatch(rule,date)

print("invalid" if matcher==None else "valid")