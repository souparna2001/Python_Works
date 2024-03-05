# note: we created class is already inherited from object class(if we given or not)
# str is working in object class
# object class is the parent for what all we created
# str is defined in object class
# @property = @decorator

class Superhero(object):    #(if we given or not :ie object)

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name

obj1=Superhero("Spiderman")
obj2=Superhero("batman")

print(obj1)     #str