import os
from classes import *
import time

def main():
    print('LOADING...')

    chars = {}

    charNames = ['buyukbabaMax','emanetoglu']

    for charName in charNames:
        currList = currentCharList()
        details = currList[charName]
        charObj = Char(details[0],details[1], details[2])
        chars.update({charName:charObj})

    firstP = chars["buyukbabaMax"]
    secondP = chars['emanetoglu']

    firstPname = input('FIRST PLAYER -> Enter your playername: ')
    secondPname = input('SECOND PLAYER -> Enter your playername: ')

    moveList = []

    time.sleep(2)

    print('{0} plays as {1}'.format(firstPname, firstP.title))
    #burda buyukbabaMax fotosu atilicak
    time.sleep(1)
    print('{0} plays as {1}'.format(secondPname, secondP.title))
    #burda emanteroglu fotosu atilicak
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

        print("AVALIABLE MOVES : \namguard --1 \nquadroDick --2 \nkucultucu --3 \ngeciktirici --4\nReverseCard --5")
        
        print('\n')

        move = input("Select by typing your moves number ->  ")
        
        if move == "1":
            if attacker.assholeArmor > 100:
                print("NIGGA YOU CANT WEAR 2 AMGUARDS AT THE SAME TIME, DAMN")
                moveList.append(Moves.invalidMove())
            else:
                Moves.amguard(attacker)
                moveList.append('amguard')

        elif move == '2':
            Moves.quadroDick(attacker)
            attacker.attack(defencer, attacker.dickSize)
            attacker.dickSize = attacker.defaultDickSize
            moveList.append('quadroDick')

        elif move == '3':
            Moves.kucultucu(defencer)
            moveList.append('kucultucu')

        elif move == '4':
            Moves.geciktirici(attacker)
            attacker.attack(defencer, attacker.dickSize)
            time.sleep(1)
            attacker.attack(defencer, attacker.dickSize)
            attacker.dickSize = attacker.defaultDickSize
            moveList.append('geciktirici')

        elif move == '5':
            Moves.ReverseCard(attacker, defencer, moveList, -1)
            moveList.append('ReverseCard')

        else:
            print("YOU DIDN'T ENTERED A VALID MOVE. YOU FOOL, WASTED YOUR TURN")

        
        time.sleep(2)
    
    print("\n"*3)
    print('KO')
    print("\n"*3)

    if firstP.hp <= 0:
        print("WINNER IS {0}".format(secondPname))
    elif secondP.hp <= 0:
        print("WINNER IS {0}".format(firstPname))




if __name__ == "__main__":
    main()