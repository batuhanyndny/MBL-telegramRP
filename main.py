import os
import cv2
from classes import *
import time

def main():
    print('LOADING...')

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

    while firstP.hp > 0 and secondP.hp > 0:

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

        print("AVALIABLE MOVES : \namguard --1 \nquadroDick --2 \nkucultucu --3 \ngeciktirici --4")
        
        print('\n')

        move = input("Select by typing your moves number ->  ")
        
        if move == "1":
            if attacker.assholeArmor > 100:
                print("NIGGA YOU CANT WEAR 2 AMGUARDS AT THE SAME TIME")
            else:
                Moves.amguard(attacker)

        if move == '2':
            Moves.quadroDick(attacker)
            attacker.attack(defencer, attacker.dickSize)
            attacker.dickSize = attacker.defaultDickSize
            

        if move == '3':
            Moves.kucultucu(defencer)

        if move == '4':
            Moves.geciktirici(attacker)
            attacker.attack(defencer, attacker.dickSize)
            time.sleep(1)
            attacker.attack(defencer, attacker.dickSize)
            attacker.dickSize = attacker.defaultDickSize


        
        time.sleep(2)
    
    if firstP.hp <= 0:
        print("WINNER IS {0}".format(secondPname))
    elif secondP.hp <= 0:
        print("WINNER IS {0}".format(firstPname))




if __name__ == "__main__":
    main()