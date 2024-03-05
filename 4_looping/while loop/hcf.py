n1=int(input("enter the number")) 
n2=int(input("enter the number")) 

sm_num=n1 if n1<n2 else n2

fact=1 
i=1 

while(i<=sm_num):
      if(n1%i==0 and n2%i==0): 
       fact=i
      i+=1 

print(fact) 





     




