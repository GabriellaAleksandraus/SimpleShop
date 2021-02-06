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





######## MAIN ########
class Actions:
    Delivery   = 0
    Sell       = 1
    Show       = 2
    Quit       = 3
    Skip       = 4

class Shop:
    def __init__(self, reader, parcer, action):
        self.reader = reader
        self.parcer = parcer
        self.action = action


    def start(self):
        stock = 0
        while True:
            text = self.reader.get_info()
            action, amount = self.parcer.parce_info(text)
            if action == self.action.Skip:
                continue
            if action == self.action.Quit:
                break
            if action == self.action.Delivery:
                stock = stock + amount
            if action == self.action.Sell:
                stock = stock - amount
            if action == self.action.Show:
                print("Stock:", stock)

reader=Command_Line_Input()
parcer=Single_Character_Parcer(Actions)

shop=Shop(reader, parcer, Actions)
shop.start()
