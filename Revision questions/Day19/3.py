# 3. Pattern print 
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *


n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*", end="")
    if i != 0:
        print(" " * ((i - 1) * 2 + 1) + "*", end="")
    print()

for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*", end="")
    if i != 0:
        print(" " * ((i - 1) * 2 + 1) + "*", end="")
    print()


# for row in range(0,8):
#     for col in range(0,8):
#         if (row+col==4) or (col-row==4) or (row+col==12) or (row-col==4):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()