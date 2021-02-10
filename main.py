from Library.Command_Line_Input import Command_Line_Input 
from Library.Single_Character_Parcer import Single_Character_Parcer
from Library.Ram_DB import Ram_DB
from Library.Actions import Actions
from Library.Shop import Shop

reader=Command_Line_Input()
parcer=Single_Character_Parcer(Actions)
saver=Ram_DB()

shop=Shop(reader, parcer, Actions, saver)
shop.start()