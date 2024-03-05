all_stud=open("C:\\Users\\souparna\\Desktop\\Python Works\\file_io\\student.txt","r")
failed_stud=open("C:\\Users\\souparna\\Desktop\\Python Works\\file_io\\failed.txt","r")


all_stud_set={st.rstrip("\n") for st in all_stud}

failed_stud_set={st.rstrip("\n") for st in failed_stud} 

passed_student=all_stud_set-failed_stud_set
print(passed_student)

                  






