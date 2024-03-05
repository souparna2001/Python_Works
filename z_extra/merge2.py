# string1="ABC"
# string2="PQR"
# string2="PQRST"

string1=input("enter the string")
string2=input("enter the string")

smallest_length=min(len(string1),len(string2))
print(smallest_length)

result=""

for i in range(0,smallest_length):
    output=string1[i]+string2[i]
    result+=output

# print(result)

# slicing     
if len(string1)>len(string2):
    rem=string1[smallest_length:]
else:
    rem=string2[smallest_length:]

result+=rem
print(result)


