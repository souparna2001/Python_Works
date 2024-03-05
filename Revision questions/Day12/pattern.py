# 3.Pattern print 
#    6 6 6 6 6 6 
#    5 5 5 5 5 
#    4 4 4 4 
#    3 3 3 
#    2 2 
#    1





row=6
for i in range(row,0,-1):
    n=i
    for j in range(0,i):
        print(n,end=" ")
    print()    
