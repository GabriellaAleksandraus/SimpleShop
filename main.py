from Library.Command_Line_Input import Command_Line_Input 
from Library.Single_Character_Parcer import Single_Character_Parcer
from Library.Ram_DB import Ram_DB
from Library.Actions import Actions
from Library.Shop import Shop

reader=Command_Line_Input() #create a reader for the shop that reads from the command line
parcer=Single_Character_Parcer(Actions) #create a parcer for the shop that communicates using actions described in Action
saver=Ram_DB()  #deciding what database the shop should use

shop=Shop(reader, parcer, Actions, saver) #create a shop that uses the defined reader, parcer, actions and saver
shop.start()    #calls the start function located in the object shop