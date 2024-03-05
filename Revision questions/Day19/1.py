# 1. Write a python program to identify unique triplets whose three elements sum to zero from an array of n integers

ar=[1,0,5,-6,10,-12,7,-3,4]
triplets=[]
a=0
for i in ar:
    for j in ar:
        t=-(i+j)
        if t in ar:
            temp_lst=[i,j,t]
            temp_lst.sort()
            while temp_lst not in triplets:
                triplets.append(list())
                triplets[a].append(i)
                triplets[a].append(j)
                triplets[a].append(t)
                triplets[a].sort()
                a+=1
print(f"sum of {triplets} is zero")                


 