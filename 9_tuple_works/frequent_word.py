word="pneumonoultramicroscopicsilicovolcanoconiosis"
wc={}

for ch in word:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1

print(wc) 