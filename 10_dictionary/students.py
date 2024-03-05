students=[
    {"id":1,"name":"jhon","skills":["c","c++"],"exp":2,"qualification":"mca"},
    {"id":1,"name":"jain","skills":["python","js"],"exp":0,"qualification":"btech"},
    {"id":1,"name":"vijin","skills":["c","java","python"],"exp":4,"qualification":"mca"},
    {"id":1,"name":"tinu","skills":["r","java"],"exp":3,"qualification":"mtech"},
    {"id":1,"name":"roy","skills":["python","css","js"],"exp":0,"qualification":"bca"},
    {"id":1,"name":"vijil","skills":["js","r","css"],"exp":1,"qualification":"mtech"},
    {"id":1,"name":"ravi","skills":["java","python"],"exp":3,"qualification":"btech"},
    {"id":1,"name":"tom","skills":["java","css","r","sql"],"exp":4,"qualification":"bca"},
    {"id":1,"name":"ryan","skills":["c","css","python"],"exp":0,"qualification":"mca"},
                                           
                                           
] 

# 1. total number of students
# print("total no of students",len(students))  

# 2. all students names
# for s in students:
#     print(s.get("name"))                            ans:one by one

# all_student_names=[s.get("name") for s in students]
# print(all_student_names)                           
# ans:in list

# 3.students names whose exp>1              
# for stud in students:
#     if stud["exp"]>1: 
#         print(stud.get("name"))         

# exp_g1=[stud.get("name") for stud in students if stud.get("exp")>1]
# print(exp_g1) 


# 4.print students whose name skills contains both java and python

# for stud in students:
#     if "java" in stud.get("skills") and "python" in stud.get("skills"):
#         print(stud.get("name")) 

                    # or

# skills_both=[stud.get("name") for stud in students if "java" in stud.get("skills") and "python" in stud.get("skills")]
# print(skills_both)


# 5.print mca student names:
# for stud in students:
#     if stud["qualification"]=="mca":
#         print(stud.get("name"))

#         # or

# mca_students=[stud.get("name") for stud in students if stud["qualification"]=="mca"] 
# print(mca_students)

      

# 6.most experienced student  

# most_exp=max(students,key=lambda d:d.get("exp"))
# print(most_exp) 

# highest_exp=most_exp.get("exp")

# exp_stud=[stud.get("name") for stud in students if stud.get("exp")==highest_exp]
# print(exp_stud) 

# 7.print students names having skills>2


# for stud in students:
#     if len(stud["skills"])>2:
#         print(stud.get("name"))

#                                        # or

# skills_2=[stud.get("name") for stud in students if len(stud["skills"])>2]
# print(skills_2)

# 8.print students name starts with j                                                                  

# for stud in students:
#     if stud["name"].startswith("j"):
#         print(stud.get("name")) 

# name_starts=[stud.get("name") for stud in students if stud["name"].startswith("j")]
# print(name_starts)
    

# 9.frequent skill in students

skill_count={}
for stud in students:
    skills=stud.get("skills")
    for sk in skills:
        if sk in  skill_count:
            skill_count[sk]+=1
        else:
            skill_count[sk]=1
print(skill_count)   



    