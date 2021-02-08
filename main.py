######## INPUT ########

class I_Input:
    def get_info(self):
        pass

class Command_Line_Input(I_Input):
    def get_info(self):
        return input()

######### PARCER #######

class I_Parce:
    def parce_info(self, text):
        pass

class Single_Character_Parcer(I_Parce):
    def __init__(self, actions):
        self.action = actions

    def parce_info(self, text):
        if len(text) == 0:
            return self.action.Skip, 0
        first_letter = text[0].upper()
        if first_letter == "L":
            return self.action.Show, 0
        if first_letter == "Q":
            return self.action.Quit, 0    
        if len(text) > 1:
            the_rest = text[1:]
            if not the_rest.isdigit():
                return self.action.Skip, 0
            amount = int(the_rest)
            if first_letter == "S":
                return self.action.Sell, amount
            if first_letter == "I":
                return self.action.Delivery, amount
        return self.action.Skip, 0

###### DATABASE ##########

class I_DB:
    def add(self, amount):
        pass
    def remove(self, amount):
        pass
    def staus(self):
        pass
    def clear(self):
        pass

class Ram_DB(I_DB):
    def __init__(self):
        self.stock = 0

    def add(self, amount):
        self.stock = self.stock + amount

    def remove(self, amount):
        self.stock = self.stock - amount

    def status(self):
        print("Stock:", self.stock)

    def clear(self):
        self.stock = 0

######## MAIN ########
class Actions:
    Delivery   = 0
    Sell       = 1
    Show       = 2
    Quit       = 3
    Skip       = 4


class Shop:
    def __init__(self, reader, parcer, action, saver):
        self.reader = reader
        self.parcer = parcer
        self.action = action
        self.saver = saver


    def start(self):
        self.saver.clear()
        while True:
            text = self.reader.get_info()
            action, amount = self.parcer.parce_info(text)
            if action == self.action.Skip:
                continue
            if action == self.action.Quit:
                break
            if action == self.action.Delivery:
                self.saver.add(amount)
            if action == self.action.Sell:
                self.saver.remove(amount)
            if action == self.action.Show:
                self.saver.status()

reader=Command_Line_Input()
parcer=Single_Character_Parcer(Actions)
saver=Ram_DB()

shop=Shop(reader, parcer, Actions, saver)
shop.start()