from Interface.I_Parce import I_Parce

class Single_Character_Parcer(I_Parce):
    def __init__(self, actions):
        self.action = actions   #store the actions we use to communicate with other modules

    def parce_info(self, text):
        if len(text) == 0:  #Empty input results in a skip action
            return self.action.Skip, 0
        first_letter = text[0].upper()  #supports both uppercase and lowercase letters
        if first_letter == "L" and len(text) == 1:  #Only L results in a show action
            return self.action.Show, 0
        if first_letter == "Q" and len(text) == 1:  #Only Q results in a quit action
            return self.action.Quit, 0    
        if len(text) > 1:   #getting the amount if there is more than one letter
            the_rest = text[1:]
            if not the_rest.isdigit():  #after the first letter, the rest should be digits
                return self.action.Skip, 0
            amount = int(the_rest)  #converts text to number
            if first_letter == "S":
                return self.action.Sell, amount
            if first_letter == "I":
                return self.action.Delivery, amount
        return self.action.Skip, 0  #if none of the above happens it results in a skip action