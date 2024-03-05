# 2. Python program to check if the given string is a palindrome.

word=input("enter the string : ")
s=""
for letter in word:
    s=letter+s
if word==s:
    print(f"{word} is palindrome") 
else:
    print(f"{word} is not palindrome")      



