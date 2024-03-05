# print()
# input()
# round()
# sum()
# min()
# max()
# sorted()
# len()
# range()
# type()


num=123.6899076
result=round(num,2)
print(result)


#  map() and filter()

# map() - 

# filter() - 

numbers=[5,6,7,8,10,11,15]

cube=list(map(lambda num:num**3,numbers))
print(cube) 

squares=list(map(lambda num:num**2,numbers))
print(squares) 



names=["python","pyx","django","hgi","pyhk"]
names_filter=list(filter(lambda w:w.startswith("py"),names))
print(names_filter) 


