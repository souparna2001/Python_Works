from re import*

year=input("enter the year")

rule="(19[0-9]{2}|20[0-9]{2})"

# rule="(19|20)[0-9]{2}"

matcher=fullmatch(rule,year)


print("invalid" if matcher==None else "valid")