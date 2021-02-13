from Interface.I_Input import I_Input

class Command_Line_Input(I_Input): #Command_Line_Input inherits from I_Input
    def get_info(self):
        return input()  #input returns text written on commandline and we return what input returns.