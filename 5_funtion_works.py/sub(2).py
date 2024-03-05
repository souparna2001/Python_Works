def smart_sub(n1,n2):
    res=n1-n2 if n1>n2 else n2-n1
    return res 

# if n1>n2:
#      return n1-n2
# else: 
#      return n2-n1

print(smart_sub(10,5))
print(smart_sub(5,10))

