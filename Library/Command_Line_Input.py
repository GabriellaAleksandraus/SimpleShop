from Interface.I_Input import I_Input

class Command_Line_Input(I_Input):
    def get_info(self):
        return input()