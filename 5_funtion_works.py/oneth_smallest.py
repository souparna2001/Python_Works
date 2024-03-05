def oneth_digit_smallest_num(n1,n2):  #n1=432,n2=18 return n1=432
    last_n1=n1%10
    last_n2=n2%10

    if last_n1<last_n2:
        return n1
    else: 
        return n2
    
print(oneth_digit_smallest_num(432,18))


