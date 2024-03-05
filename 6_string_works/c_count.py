text="pneumonoultramicroscopicsilicovolcanoconiosis"

c_count=0

for ch in text:
    if ch not in ["a","e","i","o","u"]:
        if ch.isalpha():
            c_count+=1
print(f"number of consonants={c_count}")        
print(f"Total no.of characters={len(text)}")