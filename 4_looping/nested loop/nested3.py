# 1
# 1  2
# 1  2  3 
# 1  2  3  4 
# 1  2  3  4  5


for row in range(1,6):
     for column in range(row):
        print(column,end="\t")
     print() 

# or 

# for row in range(1,6):
#     for column in range(1,row+1):
#         print(column ,end="\t")
#     print() 