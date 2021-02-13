from Interface.I_DB import I_DB

class Ram_DB(I_DB): #Ram_DB inherits from I_DB
    def __init__(self):
        self.stock = 0  #When Ram_DB is created stock is 0.

    def add(self, amount):
        if amount >= 0: #Only adds if the value of amount is positive
            self.stock = self.stock + amount    #Increases the stock by the amount

    def remove(self, amount):
        if amount >=0 and self.stock > amount:  #Can't remove more than the value of the stock.
            self.stock = self.stock - amount    #Decreses the stock by the amount.

    def status(self):
        print("Stock:", self.stock)

    def clear(self):
        self.stock = 0  #This is not necessary in a Ram data base since it always starts empty. But it might be good in another data base.