class Bank:
    def __init__(self, amount):
        self.__amount=amount
        
    def Balance(self):
        print(self.__amount)
#  
b1=Bank(999)
print(b1._Bank__amount)   #mangling
#b1.Balance()

#print(b1._amount)
# b1._amount=0
# print(b1._amount)
