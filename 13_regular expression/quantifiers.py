from re import*

text="aaabcaabbaaaabd"
#     0123456789
          
pattern="a{2,4}" #any number of a including zero numbers [a-z]* [0-9]

# a*       any no.of a including zero numbers [a-z]*[0-9]
# a{2}
# a{2,4}   

matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(count) 