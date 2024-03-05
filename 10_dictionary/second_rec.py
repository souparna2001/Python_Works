text="ABBCDA"
wc={}
dup_char=[]

for ch in text:
    if ch in wc:
        wc[ch]+=1
        dup_char.append(ch)
    else:
        wc[ch]=1
# print(dup_char)      
print(dup_char[1])        



     
