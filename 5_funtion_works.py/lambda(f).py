# add=lambda n1,n2:n1+n2
# print(add(2,4)) 

#cube

# cube=lambda n:n**3
# print(cube(2))

#-ve or +ve

# number=lambda n:"+ve" if n>0 else "-ve" if n<0 else "zero"
# print(number(5)) 

#max_2

# max_2=lambda n1,n2:n1 if n1>n2 else n2
# print(max_2(5,10)) 

#odd or even

# odd_even=lambda n:"even" if n%2==0 else "odd" 
# print(odd_even(4))   


text="good evening all"
words=text.split(" ")
srt_words=sorted(words,key=lambda w:len(w),reverse=True)
print(srt_words)  

# split - to split the string into a list
# sorted - built in funtion 
# key=lambda w:len(w) - used to take each word length , reverse=True - descending order 
                                                      # reverse=True - ascending order




#python collections

# list
# tuple
# set
# dicitionary


