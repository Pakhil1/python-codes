class bank:
    def __init__(self,amount):
        self.__amount=amount
     
    def deposit(self,amount):
        self.__value=amount
        self.__amount+=self.__value
        print("self.__value:",self.__value)
        
    def withdraw(self,amount):
        self.__value=amount
        self.__amount-=self.__value
        print("self.__value:",self.__value)
        
    def balance(self):
        print("balance",self.__amount)
        
b1=bank(777)
b1.deposit(300)
b1.withdraw(400)
b1.balance()
