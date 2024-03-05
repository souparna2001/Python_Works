class Cuisine:
    name:str
     
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
       return self.name
    
class Dish(Cuisine):
    dish_name:str
    price:int
    ingredients:str

    def __init__(self,name,dish_name,price,ingredients):
        super().__init__(name)
        self.dish_name=dish_name
        self.price=price
        self.ingredients=ingredients 

    def __str__(self):
        return self.dish_name    


dobj=Dish("chinese","noodles",45545,"lot of things")
print(dobj)
