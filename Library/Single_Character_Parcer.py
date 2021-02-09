from Interface.I_Parce import I_Parce

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