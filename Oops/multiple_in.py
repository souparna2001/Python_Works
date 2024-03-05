# multiple inheritance

# 2 parent class
# it works depends upon the inherited order



class P1:
    def m1(self):
        print("inside m1")

class P2:
    def m2(self):
        print("inside m2")

class Child(P2,P1):
    pass

ch=Child()
ch.m1()   #at first it will check the child  and go to check the inerited order given in child
ch.m2()
  

                                           # eg1

# class P1:
#     def m1(self):
#         print("inside m1")

# class P2:
#     def m1(self):
#         print("inside m2")

# class Child(P2,P1):
#     pass

# ch=Child()
# ch.m1()   #at first it will check the child  and go to check the inerited order given in child



                                           # eg2


# class P1:
#     def m1(self):
#         print("inside m1")

# class P2:
#     def m2(self):
#         print("inside m2")

# class Child(P1,P2):
#     pass

# ch=Child()
# ch.m1()   #at first it will check the child  and go to check the inerited order given in child
# ch.m2()






