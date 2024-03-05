class Bank:

    ac_num:int
    name:str 
    ac_type:str
    ifsc_code:int
    branch:str
    balance:int

# note :
             # deposit = balance + amount
             # withdraw = balance - amount

    def create_account(self,acnum,name,actype,ifsccode,branch,balance):
        # initialising instance variables
        self.ac_num=acnum
        self.name=name
        self.ac_type=actype
        self.ifsc_code=ifsccode
        self.branch=branch 
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"your{self.ac_num} has been credited with {amount} aval bal is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:    
          self.balance-=amount
          print(f"your {self.ac_num} has been debited with {amount} aval bal is {self.balance}")

    def get_balance(self):      
        print("your aval balance is ",self.balance)

ac_holder1=Bank()
ac_holder1.create_account(1234,"achu","personal",123456,"ndk",1000)
ac_holder1.deposit(700)
ac_holder1.withdraw(200)
ac_holder1.get_balance()




