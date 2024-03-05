events=[
    
    {"id":1,"name":"mrg","client":"roshan","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":2,"name":"engagement","client":"bilal","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":3,"name":"mrg","client":"manoj","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":4,"name":"birthday","client":"mobin","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":5,"name":"anniversary","client":"soumya","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":6,"name":"meeting","client":"athira","date":"12-12-2024","place":"ekm","budget":800000},
    {"id":7,"name":"xmascelebration","client":"anjali","date":"12-12-2024","place":"ekm","budget":800000},
   

]

# event_data= {"id":8,"name":"onamcele","client":"anandhu","date":"12-12-2024","place":"ekm","budget":800000}
# events.append(event_data)
# print(events)


# detatil
# id=4
# event_details=[e for e in events if e.get("id") ==id ][0]
# print(event_details)

# update
# id=1,budget=1000000,place

# id=1
# event_data=[e for e in events if e.get("id")==id]

# if event_data:
    # event_data.update({"budget":100000,"place":"Thrissur"})
# events.update({"place":"Thrissur"})
# event_data[0]["budget"]=100000
# event_data[0]["place"]="Thrissur"
# print(event_data)

id=5
event_object=[e for e in events if e.get("id")==id][0]
events.remove(event_object)

# events.pop(4)
# print(events)