# SimpleShop

## General Idea
This is a project that is suppose to manage stock balance. It is supposed to be able to contain three main functions: sell a certain amount of something, get a certain amount of deliveries and show the stock balance.

The aim of this project is to use the SOLID principes as much as possible for 
personal development. So even though the problem could be solved much easier the goal is to make it easy to update and extend some functionality. In this way, this could be done by just exchanging or updating a module instead of rewriting the whole program.

In this project, there are three independent modules: the Command_Line_Input, the Single_Character_Parcer and the Ram_DB. This means that these three could easily be updated or get some extended functionality if desired.

### I_Input
This is an interface that describes how this application expects to receive an input.

### Command_Line_Input
The Command_Line_Input gets input from the command line. 

### I_Parce
This is an interface that describes how this applications expects to parce the texts it recieves.

### Single_Character_Parcer
This parcer parces the information from a text one character at a time. 

### I_DB
This is an interface that describes what kind of functionality a database should have. 

### Ram_DB
The Ram_DB implements the functionality that I_DB describes and is responsible for how and where data is stored. You could change this database to another one who can save data between runs if you want to.

### Tests
I have made some tests but I am well aware of that they don't cover everything. 