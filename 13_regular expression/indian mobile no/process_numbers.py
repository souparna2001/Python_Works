# read valid numbers from numbers.txt

from re import*

f=open("C:\\Users\\souparna\\Desktop\\Python Works\\regular expression\\numbers.txt","r")

rule="([+]91)?[0-9]{10}"

for line in f:
    number=line.rstrip("\n")
    matcher=fullmatch(rule,number)
    if matcher!=None:
       print(number)