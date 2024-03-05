# starting with k,l,m,or n
# second place must be a digit and that  is divisible by 3
# followed by any number of alphabets and numbers


from re import*
variable_name=input("enter the variable name")
# [klmn]
rule="[k-nK-N][369][a-zA-Z0-9]"
# 369 single digit diivisble by 3 ie 3,6,9
matcher=fullmatch(rule,variable_name)

print("invalid" if matcher==None else "valid") 



