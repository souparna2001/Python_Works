# 1
# 2  2 
# 3  3  3
# 4  4  4  4
# 5  5  5  5  5         


# for row in range(1,6):
#     for column in range(row):
#         print(row,end="\t  ")
#     print()    


for row in range(1,6):
    for column in range(1,row+1):
        print(column,end="\t  ")
    print()    