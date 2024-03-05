# check if it is palindrome or not??

word=input("enter the word")
reversed_string=word[::-1]
print(f"{word} is a palindrome" if word==reversed_string else "not palindrome")

