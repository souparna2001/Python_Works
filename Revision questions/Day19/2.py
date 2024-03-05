# 2. Write a python program to make combinations of 3 digits

d1 = input("Enter the first digit: ")
d2 = input("Enter the second digit: ")
d3 = input("Enter the third digit: ")

if d1.isdigit() and d2.isdigit() and d3.isdigit() and len(d1) == len(d2) == len(d3) == 1:
    for i in d1, d2, d3:
        for j in d1, d2, d3:
            for k in d1, d2, d3:
                if i != j and j != k and k != i:
                    print(i + j + k)
else:
    print("enter valid single-digit numeric values.")
