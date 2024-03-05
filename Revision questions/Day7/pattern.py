# 3.Pattern print
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3 
# 4 4  
# 5

rows=5
for row in range(1,6):
    for column in range(1,rows-row+2):
        print(row,end=" ")
    print()





