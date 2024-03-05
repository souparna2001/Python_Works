class Student:
    name:str
    roll_no:int
    course:str

    def set_stud(self,name,rollno,course):
        self.name=name
        self.roll_no=rollno
        self.course=course

    def display_stud(self):
        print(self.name,self.roll_no,self.course)    

stud1=Student()
stud1.set_stud("Souparna",7,"CSE")

stud2=Student()
stud2.set_stud("Najiya",28,"CSE")

stud3=Student()
stud3.set_stud("Sreelaksmi",32,"CSE") 

stud4=Student()
stud4.set_stud("Mugadhri",4,"CSE")


stud1.display_stud()
stud2.display_stud()
stud3.display_stud()
stud4.display_stud()
