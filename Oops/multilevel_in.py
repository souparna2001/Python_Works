# multilevel inheritance

  # 2 parents



class Parent1:
    def m1(self):
        print("inside parent1 m1 method")

class Parent2(Parent1):
    def m2(self):
        print("inside parent2 m2 method")

class Child(Parent2):
    def c(self):
        print("inside chid c method")

ch=Child()      
ch.c()       #already defined in child class

ch.m2()      #(m2 in parent2 is inherited by child)
ch.m1()      #(m1 in parent1 is inherited by parent2 , because child is already inherited parent2 )
