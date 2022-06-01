from dataclasses import asdict
from logging import setLogRecordFactory
from re import S
import time


def charclass():
    global selfCL
    selfCL = input ("What class would you like to select? Your choices are as follows: Mage, Rogue, and Knight ")
    if selfCL.lower() == "mage" or selfCL.lower() == "rogue" or selfCL.lower() == "knight":
        time.sleep(1)
        print ("You have selected " + selfCL.title() + " as your class!")
        selfCL = selfCL.title()
    else:
        print ("You did not select an appropriate class. Please enter Mage, Rogue, or Knight.")
        time.sleep(1)
        charclass()


def start():
    startvar = input ("""Hail, adventurer. Would you like to access the inventory interface?
    """)
    startvar.strip()
    if startvar.lower() == "yes" or startvar.lower() == "y":
        global startWPN
        print("Loading inventory...")
        if selfCL == "Mage":
            #variable = name , weight , dmg
            WPN = { 'type' : 'Staff' , 'weight' : 3.8 , 'dmg' :14 }
            startWPN = WPN
            print ("Your class weapon is the " + WPN['type'] )
        elif selfCL == "Rogue":
            WPN = { 'type' : 'Dagger' , 'weight' : 1.1 , 'dmg' :8 }
            startWPN = WPN
            print ("Your class weapon is the " + WPN['type'] )
        else:
            WPN = { 'type' : 'Longsword' , 'weight' : 4.4 , 'dmg' :17 }
            startWPN = WPN
            print ("Your class weapon is the " + WPN['type'] )

    elif startvar.lower() == "no" or startvar.lower() == "n":
        print("See you next time!")
    else:
        print("Sorry, we didn't quite get that. Please try entering your response again, and respond with 'Y/YES/N/NO'.")
        time.sleep(1)
        start()
charclass()
start()


##Seems kind of sluggish. I've used lists to add a weapon feature, a weapon which changes based on class. It is indeed stored, but the stats are the only thing stored. I think I'd need to create a separate inventory, which I'll try doing below.
inventory = (startWPN['type']) #note, this code isn't integrated into the code above, it's just there for testing. works great.
print (inventory)