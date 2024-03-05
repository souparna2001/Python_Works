                                    #  LIST METHODS   #


# append() - to add an element to the end of the list
# extend() - to add an element(letters) into a list one by one to the end of the list
# count() - to get the count of the element in the list
# index() - to get the index of the element
# pop() -  if we not pass anything to pop ,the list will automatically remove the last element in the list
# pop(1) - it will remove the index of the element that we need to pop 
# insert - used to insert an element into the list,also mention the index number to insert
# remove() - to remove the element from the list
# copy() - to copy the element for new list from another list
# reverse() - to reverse the element of the list
# sort() - to sort the list in ascending order
# sort(reverse=True) - to sort elements in ascending to descending order





# append - to add an element to the end of the list

# orders=["friedrice","gheeroast","vb","cb","bb"]
# orders.append("tea")
# print(orders) 

# extend - to add an element  (letters) into a list one by one to the end of the list

# orders=["friedrice","gheeroast","vb","cb","bb"]
# orders.extend("tea")
# print(orders)


# count - to get the count of the element in the list
                                                         
# orders=["friedrice","gheeroast","vb","cb","bb","vb","cb","vb","cb"]
# print(orders.count("cb")) 


# index - to get the index of the element

# print(orders.index("gheeroast"))

                                            # pop

# print(orders.pop())      - if we not pass anything to pop ,the list will automatically remove
#                            the last element in the list


# orders.pop(1)     - it will remove the index of the element that we need to pop 
# print(orders)  


                                          # insert 

# orders.insert(1,"goby")
# print(orders)

                                           # remove

# orders.remove("friedrice")
# print(orders)

                                           # copy

# mobin_fav=["black","white","yellow","green"]
# manoj_fav=mobin_fav.copy()
# manoj_fav.remove("yellow")
# # print(manoj_fav)
# print(mobin_fav)

                                            # reverse 

# manoj_fav.reverse()
# mobin_fav.reverse()
# print(manoj_fav)
# print(mobin_fav)

                                            # sort 

# mobin_fav.sort()
# print(mobin_fav)

                                           #  sort reverse

# mobin_fav.sort(reverse=True)
# print(mobin_fav)