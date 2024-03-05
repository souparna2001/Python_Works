from json import load

f=open("C:\\Users\\souparna\\Desktop\\Python Works\\12_json_work\\students\\students.json","r")

data=load(f)


all_names=[emp.get("name") for emp in data]
print(all_names) 

# set comprehension 
# all_dept={emp.get("department") for emp in data}
# print(all_dept)  

# max_sal=max(data,key=lambda d:d.get("salary"))
# print(max_sal)





