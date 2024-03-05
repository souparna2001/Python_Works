# find longest word without using built in funtions
words=["","","","",""]
max_word=words[0]

for i in range(1,len(words)): 
  current_word=words[i] 
  if len(current_word)>len(max_word):
     max_word=words[i]               
print(max_word)  



