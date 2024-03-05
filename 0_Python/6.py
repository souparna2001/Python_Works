# 6.Write a program to check whether the character is vowel or not. 

character=input("enter the string : ")

if len(character) == 1 and character.isalpha():

    vowel="aeiouAEIOU"
    if character in vowel:
        print(f"entered character {character} is a vowel")
    else:
        print(f"{character} is not a vowel")   






                                                   #  or #



# user_char = input("Enter a character: ") 
# if len(user_char) == 1 and user_char.isalpha():
#     vowels = "aeiouAEIOU"
#     if user_char in vowels:
#         print(f"{user_char} is a vowel.")
#     else:
#         print(f"{user_char} is not a vowel.")
# else:
#     print("Please enter a single alphabetic character.")

