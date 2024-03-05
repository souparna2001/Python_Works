vehicles=[
   
    {"id":1,"name":"passionpro","brand":"hero","price":100000},
    {"id":2,"name":"xpulse","brand":"hero","price":140000},
    {"id":3,"name":"trumph","brand":"triumph","price":300000},
    {"id":4,"name":"hunter","brand":"royal","price":200000},
    {"id":5,"name":"ola s1","brand":"ola","price":170000},
    {"id":6,"name":"ather 400","brand":"ather","price":180000},


]

# list of dictionary

                                              # print all vehicle names

# for bikes in vehicles:
#     print(bikes.get("name")) 
# for bikes in vehicles:
#     print(bikes.get("brand"))  

# for bike in vehicles:
#     if bike.get("brand")=="hero":
#        print(bike.get("name"))

# hw

                                       # bikes available under 150000?
# for bikes in vehicles:
#     if bikes["price"]<150000:
#      print(bikes)


                                       # costly bike?  

# bike_list=[]
# for bikes in vehicles:
#    bike_list.append(bike.get("price"))
#    max_price=max(bike_list)   
# print(max_price)
# for bike in vehicles:
#     if bike.get("price")==max_price:
#         print(bike)

                                      # costly bike?

# costly_bike=max(vehicles,key=lambda d:d.get("price"))
# print(costly_bike)       

                                    # low cost bike

# lowcost_bike=min(vehicles,key=lambda d:d.get("price"))
# print(lowcost_bike)                              