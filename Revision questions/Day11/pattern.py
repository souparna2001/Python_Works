#                 3.Pattern print 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5


for row in range(0,6):
    for col in range(1,row+1):
        print(col,end=" ")
    print("")    