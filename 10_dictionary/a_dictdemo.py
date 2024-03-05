                                      # dictionary 

# index not supported
# dict={"key":value}
# key value in lowercase



student={"rollno":7,"name":"Souparna","dept":"cse","batch":"B","college":"Sahrdaya","place":"Nandikkara","marks":450}
# print(student)

print(student["name"])
print(student["rollno"])

# student["marks"]=500
# print(student)


                                       # dictionary methods #



#                                         keys() : return all keys

product={"code":1001,"name":"orange","price":35}

# print(product["price"])  

# for k in product.keys():
#     print(k)


#                                          values()

# for v in product.values():
#     print(v) 

#                                          items()

# for k,v in product.items():
#     print(k,v)  

#                                          get() - doesn't return any error


# print(product.get("pricess")) 
# print("here") 


# product["price"]=50
# print(product) 
                        
#                                         update() - to update the values

# product.update({"name":"green"})         
# print(product)

product.update({"code":200})
print(product)

# #                                         pop() - to remove values

# product.pop("price")
# print(product)


