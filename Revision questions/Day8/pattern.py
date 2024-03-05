# 3.Pattern print 
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *


for i in range(5,0,-1):
    for j in range(1,i+1):
             print(" ",end="")
    for k in range(j,6):
            print("*",end="")
    print()        
