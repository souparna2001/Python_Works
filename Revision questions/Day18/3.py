# 3. Pattern print 
#       A 
#      A B 
#     A B C 
#    A B C D 
#   A B C D E

i=64
for row in range(1, 6):
    
    for col1 in range(1, 6 - row):
        print("", end=" ")
    for col2 in range(1, row + 1):
        print(chr(i+ col2), end=" ")
    print()
    
    
    


