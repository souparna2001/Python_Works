f=open("C:\\Users\\souparna\\Desktop\\Python Works\\11_file_io\\news.txt","r")
for line in f:
    words=line.rstrip("\n").split(",")   #  'fat cat'
    #words=line.rstrip("\n").split(" ") #   ["fat","cat"]
    print(words)  

# f=open("C:\\Users\\souparna\\Desktop\\Python Works\\11_file_io\\news.txt","r")
# for line in f:
#     print(line,end="")

                                        
                                     #  total no.of words 

wc={} 
for line in f:  #line=fat cat
     words=line.rstrip("\n").split(" ") #["fat","cat"]
     for w in words:
          if w in wc:
               wc[w]+=1
          else:  
               wc[w]=1 
print(wc)  







