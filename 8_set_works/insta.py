# insta_users={"mohanlal","prithvi","dq","vijay","fahad","sureshgopy","lalu"}
# mohanlal_followings={"prithvi","vijay","lalu"}
# dq_friends={"prithvi","fahad","sureshgopy","lalu"}

# #mohanlal suggestions

# suggestions_mohanlal=insta_users.difference(mohanlal_followings)
# suggestions_mohanlal.remove("mohanlal")
# print(suggestions_mohanlal)

# mutual_friends=mohanlal_followings.intersection(dq_friends)
# print(mutual_friends) 

order1={"cb","tika","fishfry","friedrice","vb","gheeroast"}
order2={"cb","friedrice","nan","upuma","vegmeals","idly"} 


# either elements in set 1 or set 2 not in both

u_set=order1.union(order2)
inter_section_set=order1.intersection(order2)
new_order=u_set.difference(inter_section_set)
print(new_order)

new_order=u_set.symmetric_difference(order2)
print(new_order)


st1={10,20,30}
st2={100,200,300}

st1.update(st2)
print(st1)