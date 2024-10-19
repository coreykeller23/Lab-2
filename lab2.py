"""
Corey Keller
File Name: Lab2
Version 1.0
Creation: 1.24.24
Updated: 1.25.24
Purpose: The program should be used to convert Dungeons and Dragons currency into other types of currencies.
The variables named starting(cointype) represent the amount of gold that the user inputs to figure out how much of another coin they have.
The variables named after coin types represent the values used in determining the conversion from gold to another coin type.
The float variables are used to round off platinum, as it is a higher value coin, resulting in decimals when converting from gold.
Other variables should result in integers, unless the user inputs a gold value that has more than 3 decimal place values.
"""

#This line marks the start of variable creation regarding the value of currency in comparison to gold.
gold = 1
copper = 100
silver = 10
platinum = float(.1)
electrum = 2
startingGold1 = 42
startingGold2 = 76
startingGold3 = 32
startingGold4 = 87
startingGold5 = 64

#This line marks the beginning of formulas for conversion rates using the varibales created.
goldAmount = int(gold/gold*startingGold1)
copperAmount = int(copper/gold*startingGold2)
silverAmount = int(silver/gold*startingGold3)
platinumAmount = float(platinum/gold*startingGold4)
electrumAmount = int(electrum/gold*startingGold5)

#This line marks the string variables used to create the paragraph.
goldMessage = "The amount of gold that " + str(startingGold1) + " gold is in terms of gold is " + str(goldAmount) + ". "
copperMessage = "The amount of copper that " + str(startingGold2) + " gold is in terms of copper is " + str(copperAmount) + ". "
silverMessage = "The amount of silver that " + str(startingGold3) + " gold is in terms of silver is " + str(silverAmount) + ". "
platinumMessage = "The amount of platinum that " + str(startingGold4) + " gold is in terms of platinum is " + str(round(platinumAmount, 1)) + ". "
electrumMessage = "The amount of electrum that " + str(startingGold5) + " gold is in terms of electrum is " + str(electrumAmount) + ". "

#This line marks the beginning of the paragraph using the variables.
sentenceBegin = "The conversion rates of Dungeons and Dragons currency from gold to other forms of currency is easy to comprehend. "
sentenceEnd = "Using this, you can apply any amount of gold to find out how much money you have in different coinage."
#The messages and sentences are combined to make the paragraph.
message = sentenceBegin + "\n" + goldMessage + "\n" + copperMessage + "\n" + silverMessage\
+ "\n" + platinumMessage + "\n" + electrumMessage + "\n" + sentenceEnd
print(message)