import os
import cv2
from classes import *
import time

def main():
    print('KARAKTERLER HAZIRLANIYOR')

    chars = {}

    for char in os.listdir('chars/'):
        charImg = cv2.imread(char)
        charName = char.split('.')[0]
        currList = currentCharList()
        details = currList[charName]
        charObj = Char(details[0],details[1], details[2])
        chars.update({charName:charObj})

    firstP = chars["buyukbabaMax"]
    secondP = chars['emanetoglu']

    firstPname = input('FIRST PLAYER -> Enter your playername: ')
    secondPname = input('SECOND PLAYER -> Enter your playername: ')

    time.sleep(2)

    print('{0} plays as {1}'.format(firstPname, firstP.title))
    time.sleep(1)
    print('{0} plays as {1}'.format(secondPname, secondP.title))
    time.sleep(1)

    attacker, defencer = setTurnOrder(firstP, secondP)

    Attacker = enumerate(attacker)
    Defencer = enumerate(defencer)

    countDown()

    while firstP.hp > 0 or secondP.hp > 0:

        attacker = Attacker.__next__()[1]

        defencer = Defencer.__next__()[1]
        print('\n')
        turnDef(attacker)
        print('\n')
        time.sleep(1)
        print('\n')
        healthStatus(firstP, secondP)

        time.sleep(2)

        print('\n')

        print("AVALIABLE MOVES : \namguard --1 \nquadroDick --2 \nsedativeDick --3 \ngeciktirici --4")
        
        print('\n')

        move = input("Select by typing your moves number ->  ")
        
        if move == "1":
            Moves.amguard(attacker)

        if move == '2':
            Moves.quadroDick(attacker)
            attacker.attack(defencer, attacker.dickSize)
            

        if move == '3':
            Moves.sedativeDick(defencer)

        if move == '4':
            Moves.geciktirici(attacker)
            attacker.attack(defencer, attacker.dickSize)

        time.sleep(1)

        
        time.sleep(2)

def healthStatus(firstP, secondP):
    firstP_healthBar, firstP_percent = do_health(firstP.hp, firstP.defaultHP)
    secondP_healthBar, secondP_percent = do_health(secondP.hp, secondP.defaultHP)
    print("########################################## HEALTH STATUS ##########################################\n#                          {0}'s health is {1} - {2} {3}\n#                          {4}'s health is {5} - {6} {7}\n###################################################################################################".format(firstP.title, firstP.hp, firstP_healthBar, firstP_percent, secondP.title, secondP.hp, secondP_healthBar, secondP_percent))

def turnDef(Char):
    print("------------------{0}'s TURN------------------".format(Char.title))
    return Char

def setTurnOrder(Char1, Char2):
    Attacker = []
    Defencer = []
    for _ in range(100):
        Attacker.append(Char1)
        Attacker.append(Char2)
    for _ in range(100):
        Defencer.append(Char2)
        Defencer.append(Char1)
    return Attacker, Defencer

if __name__ == "__main__":
    main()