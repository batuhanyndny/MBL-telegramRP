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

    defMoves = currentMoveList()

    roundCounter = 1

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

        roundNumber = AnnounceRoundNumber(roundCounter)
        time.sleep(1)

        print('\n')
        turnDef(attacker)
        print('\n')
        time.sleep(1)
        print('\n')
        healthStatus(firstP, secondP)

        time.sleep(2)

        print('\n')
        
        movesDict = setAvaliableMoves(roundNumber, defMoves['regular'], defMoves['legendary'])

        moveNames, moveValues = list(movesDict.values()) , list(movesDict.keys())

        print("AVALIABLE MOVES : \n{0} --{1} \n{2} --{3} \n{4} --{5} \n{6} --{7}".format(moveNames[0], moveValues[0], moveNames[1], moveValues[1], moveNames[2], moveValues[2], moveNames[3], moveValues[3]))
        
        print('\n')

        moveValue = input("Select by typing your moves number ->  ")

        try:
            move = movesDict[int(moveValue)]
        except:
            print("YOU DIDN'T ENTERED A VALID MOVE. YOU FOOL, WASTED YOUR TURN")
            move = 'invalid'
            moveList.append('invalidMove')


        if move == "amguard":
            Moves.amguard(attacker)
            moveList.append('amguard')

        elif move == 'quadroDick':
            Moves.quadroDick(attacker, defencer)
            moveList.append('quadroDick')

        elif move == 'kucultucu':
            Moves.kucultucu(defencer)
            moveList.append('kucultucu')

        elif move == 'geciktirici':
            Moves.geciktirici(attacker, defencer)
            moveList.append('geciktirici')
            
        elif move == 'ReverseCard':
            Moves.ReverseCard(attacker, defencer, moveList, -1)
            moveList.append('ReverseCard')

        elif move == 'dickSlap':
            Moves.dickSlap(attacker, defencer)
            moveList.append('dickSlap')

        elif move == 'spankDaddy':
            Moves.spankDaddy(attacker, defencer)
            moveList.append('spankDaddy')

        elif move == 'assholeVacuum':
            Moves.assholeVacuum(attacker, defencer)
            moveList.append('assholeVacuum')
            

        
        time.sleep(1)

        roundCounter += 0.5

    
    print("\n"*3)
    print('SWINGING SEMEN SHOT')
    print("\n"*3)

    if firstP.hp <= 0:
        print("WINNER IS {0}".format(secondPname))
    elif secondP.hp <= 0:
        print("WINNER IS {0}".format(firstPname))




if __name__ == "__main__":
    main()