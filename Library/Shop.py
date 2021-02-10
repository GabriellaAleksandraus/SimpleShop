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