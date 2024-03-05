text="ABCABBDE"
# print first recursive character
wc={}
for ch in text:
    if ch in wc:
        print("first recusrvive character is",ch)
        break
    else:
        wc[ch]=1
      

