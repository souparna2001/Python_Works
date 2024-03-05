# kerala vehicle numbers

# start with kl
# 2 digit
# 1 or 2 alphabet
# 4 digits

from re import *
vehicle_number=input("enter vehicle number")
# rule="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}" 
rule="(KL)-[0-9]{2}-[A-Z]{1,2}-[0-9]{4}"                    # include - to the output
# rule="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"         # means that - is optional   (-)?
matcher=fullmatch(rule,vehicle_number)
print("invalid" if matcher==None else "valid")



