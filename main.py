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

    print("MATCH BEGINS")
    time.sleep(2)

    while firstP.hp > 0 or secondP.hp > 0:

        print("--{0}'s TURN--".format(firstPname))
        print("HEALTH STATUS: \n {0}'s health is {1} \n{2}'s health is {3}".format(firstPname, firstP.hp,secondPname, secondP.hp))

        time.sleep(2)

        print("AVALIABLE MOVES : \namguard --1 \nquadroDick --2 \nsedativeDick --3 \ngeciktirici --4")
        move = input("Select by typing your moves number")
        
        if move == '2':
            ds = firstP.move(Moves.quadroDick(firstP))
            firstP.attack(secondP, ds)
        
        time.sleep(2)

        print("HEALTH STATUS: \n {0}'s health is {1} \n{2}'s health is {3}".format(firstPname, firstP.hp,secondPname, secondP.hp))

        break

if __name__ == "__main__":
    main()