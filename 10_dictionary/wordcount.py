text="hello hai hello hai"
words = text.split(" ")
wc = {}

for w in words:
    if w in wc:
        wc[w] += 1
    else:
        wc[w] = 1
print(wc)           

# hello 2
# hai   2 


