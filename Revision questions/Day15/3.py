# 3. Pattern print 
# A 
# B B 
# C C C 
# D D D D 
# E E E E E

i=65
for row in range(1, 6):
    for col2 in range(1, row + 1):
        print(chr(row+64), end=" ")
        i += 1
    print(" ")