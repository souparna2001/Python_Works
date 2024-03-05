# Write a program to accept percentage from the user and display the grade according to the following criteria
# Mark > 90 =A Grade
# >80 and <= 90 = B Grade
# >=60 and <= 80 =C Grade
# Below 60 = D grade

mark=int(input("enter the mark of student "))

if mark>=90:
    print("A grade")
elif mark>80 and mark<=90:
    print("B grade")   
elif mark>=60 and mark<=80:
    print("C grade")   
elif mark<60:
    print("D grade")
else:
    print("failed")              