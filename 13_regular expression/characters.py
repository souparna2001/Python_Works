from re import*

text="kaBczabc 9@7c"

pattern="[ac]"   
# []   
# [ac]               a or c
# [abc]              a or b or c 
# [a-e]              sequence of characters
# [a-z]              lowercase a to z
# [A-Z]              uppercase A to Z
# [a-zA-Z]           matches all alphabets
# [0-9]              check for all digits
# [a-zA-Z0-9]        alphanumeric characters
# [^a-z]             excluding a-z
#[^a-zA-Z0-9]        return special characters
# \d                 equalent of 0-9 
# \D                 excluding 0-9   
# \w                 alphanumeric [a-zA-Z0-9]  


matcher=finditer(pattern,text) 

for m in matcher:
    print(m.start(),m.group())  



