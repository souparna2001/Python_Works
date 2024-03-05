# Take input of age of 3 people by user and determine oldest and youngest among them.
# age1=int(input("enter the age"))
# age2=int(input("enter the age"))
# age3=int(input("enter the age"))

# if age1>age2 and age1>age3:
#     print("age1 is oldest")
# else:
#     print("age1 is youngest")


# if age2>age1 and age2>age3:
#     print("age2 is oldest")
# else:
#     print("age2 is youngest")

# if age3>age1 and age3>age2:
#     print("age3 is oldest")
# else:
#     print("age3 is youngest")

age1=int(input("enter the age"))
age2=int(input("enter the age"))
age3=int(input("enter the age"))

if age1>age2 and age1>age3:
    print("age1 is the oldest")

elif age2>age1 and age2>age3:
    print("age2 is the oldest")

elif age3>age1 and age3>age2:
    print("age3 is the oldest")

if age1<age2 and age1<age3:
    print("age1 is the youngest")

elif age2<age1 and age2<age3:
    print("age2 is the youngest")

elif age3<age1 and age3<age2:
    print("age3 is the youngest")       

