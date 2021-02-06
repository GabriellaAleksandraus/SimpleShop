class Shop:

    def start(self):
        stock = 0
        while True:
            text = input()
            first_letter = text[0].upper()
            if len(text) > 1:
                amount = int(text[1:])
                if first_letter == "S":
                    stock = stock - amount
                if first_letter == "I":
                    stock = stock + amount   
            if first_letter == "L":
                print("Stock:", stock)
            if first_letter == "Q":
                break
shop=Shop()
shop.start()
