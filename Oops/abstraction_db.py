from abc import ABC, abstractmethod

class Dbconnect(ABC):
      
      def __init__(self,user,password,port,database):
            pass
      
      @abstractmethod
      def connect(self):
            pass
      @abstractmethod
      def execute_query(self):
            pass
      @abstractmethod
      def close(self):
            pass


class MyDb(Dbconnect):
      
      def __init__(self, user, password, port, database):
            self.user=user
            self.password=password
            self.port=port
            self.database=database


      def connect(self):
            print("db connect")

      def execute_query(self):
            print("db execute query")

      def close(self):
            print("db close")  

obj=MyDb("FF","dfghj*5g",34,"fdg")                
obj.connect()