class Shop:
    def __init__(self, reader, parcer, action, saver):  #stores all the dependent modules for the shop
        self.reader = reader    #responsable for the communictions into the shop. Might be nice if the reader also would be responsable for communications out from the store. 
        self.parcer = parcer    #translates text to actions
        self.action = action    #represents the possible actions that shop can take
        self.saver = saver      #responsable for storing and retreiving information


    def start(self):    #starts the shop
        self.saver.clear()  #according to specifications, the shop should start empty
        while True:
            text = self.reader.get_info()   #text contains the information about the next order
            action, amount = self.parcer.parce_info(text)   #translates the text into actions and amount
            if action == self.action.Skip:
                continue    #goes to the beginning of the while loop
            if action == self.action.Quit:
                break   #Stops the while loop
            if action == self.action.Delivery:
                self.saver.add(amount)  #tells the saver how much to add
            if action == self.action.Sell:
                self.saver.remove(amount) #tells the save how much to remove
            if action == self.action.Show:
                self.saver.status() #Shows status