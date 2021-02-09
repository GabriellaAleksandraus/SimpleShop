from Library.Command_Line_Input import Command_Line_Input 
from Library.Single_Character_Parcer import Single_Character_Parcer
from Library.Ram_DB import Ram_DB

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