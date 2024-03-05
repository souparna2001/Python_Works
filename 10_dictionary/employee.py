employee={"id":1000,"name":"hari","department":"developer","salary":70000}

# employee["department"]="senior developer"

employee.update({"department":"senior developer"})

# if salary not present add salary as 45000 else add bonus of 10000 

if "salary" not in employee:
    
    employee["salary"]=45000
else:
    employee["salary"]+=1000

print(employee)                                                    

                                                             

