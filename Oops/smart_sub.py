# decorator

def swap_sum(fn): #fn=sub(2,10)
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)   
    return wrapper 

@swap_sum
def sub(n1,n2):
    return n1-n2

@swap_sum
def div(n1,n2):
    return n1/n2 

print(sub(2,10))
print(div(2,10))


