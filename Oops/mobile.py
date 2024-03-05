class Mobile:

    name:str
    brand:str
    display:str
    price:int

    def __init__(self,name,brand,display,price):
        self.name=name
        self.brand=brand
        self.display=display
        self.price=price

    def display_mobile(self):
        print(self.name,self.brand,self.display,self.price)    
    
    def __str__(self):
        return self.name 
    
obj=Mobile("s23 ultra","samsung","amoled",134000)
obj.display_mobile()

print(obj)