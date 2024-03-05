
# def add(n1,n2):
#     return n1+n2

# def add(n1,n2,n3):
#     return n1+n2+n3

# def add(n1,n2,n3,n4):
#     return n1+n2+n3+n4

# this is not applicable in python because it takes only the recently implemented.so that is y we come up with args

# same funtion name different number of parameters is called funtion overloading 

# -> In python they will consider only the recently implemented .

    # instead of supporting funtion overloading in python , args it is equavalent to funtion overloading.
    # *args - for passing number of parameters
    #       - accepting parameters in the form of tuple (o/p is)


# def add(*args):
#     print(args)

# add(10,20,30,40)
# add(10,20)
# add(1,2,3,4,5,6)
# add()    


# def product(*args):
#     print(args)

# product(10,20,30,40)

def product(*args):
    result=1
    for n in args:
        result=result*n
    return result
print(product(10,20))
print(product(10,20,30,40))

def addition(*args):
    return sum(args)

print(addition(10,20))
print(addition(10,20,30,40))  

def last_digit_sum(*args):
    last_digit=[n%10 for n in args]
    return sum(last_digit)

print(last_digit_sum(12,14,132))


#  ? last digit maximum
                        # 123,134,135,18,19

def last_digit_max(*args):
    digit=[n%10 for n in args]
    return max(digit)

print(last_digit_max(18,11,12,9))


# **kwargs : keyword arguments 
#  accepting dictionary
# bcs key:value 2 is there , so **kwargs


# def add_employee(**kwargs):
#     print(kwargs.get("name"))
#     print(kwargs.get("salary"))

# add_employee(id=19,name="hari",n_place="ekm",w_place="tvm",salary=24000)


def my_fun(*args,**kwargs):
    print(args)
    print(kwargs)

my_fun(1,2,3,4,reverse=True) 



def last_digit_sort(*args,**kwargs):

    digits=[n%10 for n in args]
    value=kwargs.get("reversed")
    if value==True:
        digits.sort("reversed")
    else:
        digits.sort()
    return digits 


print(last_digit_sort(17,12,14,3,1,reversed=False)) 



