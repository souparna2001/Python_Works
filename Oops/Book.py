class Book:

    name:str 
    author:str 
    pages:int
    prices:int 

    def __init__(self,name,author,pages,prices):
        self.name=name
        self.author=author
        self.pages=pages
        self.prices=prices

    def display_book(self):
        print(self.name,self.author,self.pages,self.prices)

    def __str__(self):
        return self.name    

obj1=Book("Half Girlfriend","chetan bhagat",150,260) 
obj2=Book("its ends with us","cooleen hoover",200,500)    
obj3=Book("its starts with us","cooleen hoover",200,500) 
# obj.display_book()

print(obj1)
print(obj2)
print(obj3)