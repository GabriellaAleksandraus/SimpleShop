from Interface.I_DB import I_DB

class Ram_DB(I_DB):
    def __init__(self):
        self.stock = 0

    def add(self, amount):
        if amount >= 0:
            self.stock = self.stock + amount

    def remove(self, amount):
        if amount >=0 and self.stock > amount:
            self.stock = self.stock - amount

    def status(self):
        print("Stock:", self.stock)

    def clear(self):
        self.stock = 0