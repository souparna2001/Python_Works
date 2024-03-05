# method overriding

 # minimum 2 class
 # 2 class  "is-a" relation ship
 # mobile is the method that overrided by child
 # if child class is not ok with the implementation of parent class , child class can provide implementation by itself .  

class Parent:

   def mobile(self):
       print("redmi note 12")

   def vehicle(self):
       print("splender")

class Child(Parent):

    def mobile(self):
        print("iphones15")

ch=Child()
ch.mobile()
ch.vehicle()  

   