    #                * 
    #             *     *
    #           *    *    *
    #         *    *    *   *
    #       *    *    *   *    *  


# 3 loops needed 

rows = 5

# Outer loop for each row
for i in range(1, rows + 1):
    # Inner loop for leading spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # Inner loop for printing stars
    for k in range(2 * i - 1):
        print("*", end="")
    
    # Move to the next line after completing a row
    print()

    


