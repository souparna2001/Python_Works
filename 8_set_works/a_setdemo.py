# define
# insertion order is not preserved , index is not supported
# mutable
# methods





 
# st={10,20}
# print(type(st))                    #set

# st={}
# print(type(st))                    #dict

# lst=[]                             # or list()         empty list
# tp=()                              # or tuple()        empty tuple
# # set=set()                                            empty set
# dict={}                            # or dict()         empty dictionary

# # st={10,20,"hello",True}            #insertion order is not preserved
# # print(st[0])                       #index is not supported

# st={10,20,"hello",True,10,20}        #duplicates not allowded
# print(st)

                        ####################set methods######################

                
                                  # add()

# colors={"red","green","blue"}
# colors.add("yellow")
# print(colors) 

                                  # intersection

# st1={"red","green","blue"}
# st2={"purple","yellow","cyan","blue"}

# inter_set=st1.intersection(st2)
# print(inter_set)

                                  #  union

# union_set=st1.union(st2)
# print(union_set) 

                                  #difference

# diff_set=st1.difference(st2)
# print(diff_set)

# # diff_set=st2.difference(st1)
# print(diff_set) 

                                  # pop 

# st1.pop()
# print(st1) 


                                # remove : - element should present otherwise will get an error and code will be terminated.

# st1.remove("red")
# print(st1) 

# discard - code will not be terminated.

# st1.discard("red")
# print(st1)


# symmetric_difference

# update()