from  abc import ABC,abstractmethod 

class Car(ABC):

    def __init__(self,name,brand,model):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def acclerate(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Swift(Car):

    def __init__(self, name, brand, model):
       self.name=name
       self.brand=brand
       self.model=model

    def start(self):
        print("car starts")

    def acclerate(self):
        print("car acclerates")  

    def stop(self):
        print("car stops") 

new=Swift("jnfkd","bdan","dhbjd")
# print(new.name)
new.stop()
           



  
