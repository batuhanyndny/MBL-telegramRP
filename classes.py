'''
TODO
-Moves
    

-CHARS


'''

import random
import time

class Char:

    title = ''
    details = ''
    is216 = False
    hp = 420
    assholeArmor = 69
    assholeSize = 1
    dickSize = 7

    hasBlock = False

    defaultAssholeArmor = 69
    defaultDickSize = 7
    defaultHP = 420
    

    def __init__(self,title, dickSize, details):
        self.title = title
        self.dickSize = dickSize
        self.defaultDickSize = dickSize
        self.details = details

    
    def attack(self,Char, damage):
        if Char.hasBlock:
            print("NAH MAN YOUR ATTACK JUST GET BLOCKED")
        else:
            if Char.assholeArmor > 0:
                if damage > Char.assholeArmor:
                    print("PRO GAMER ATTACKK !! {0}'s ASSHOLE ARMOR JUST BROKE !! PREPARE FOR RAPE".format(Char.title))
                    Char.hp -= damage-Char.assholeArmor
                    Char.assholeArmor = 0
                elif damage < Char.assholeArmor:
                    print("ARMOR HIT !! {0}'s asshole protector damaged by {1}".format(Char.title,damage))
                    Char.assholeArmor -= damage
            else:
                print("Hit !! {0}'s health decrased by {1}".format(Char.title, damage))
                Char.hp -= damage

class Moves:

    def invalidMove():
        return 

    def amguard(attacker):#legendary
        attacker.assholeArmor += 80
        print('{0} HAS GAINED 80 ASSHOLE ARMOR'.format(attacker.title))
        time.sleep(2)


    def quadroDick(attacker, defencer):#legendary
        print("{0}'s dick size increased to {1} cm NOW HAS x4 DAMAGE".format(attacker.title, attacker.dickSize*4))
        attacker.dickSize = attacker.dickSize*4
        attacker.attack(defencer, attacker.dickSize)
        resetDS(attacker)
        time.sleep(2)

    def kucultucu(defencer): #legendary
        defencer.dickSize = 2
        print("{0}'s dick size decrased to 2 cm DAMN NIGGA MICROPENIS".format(defencer.title))
        time.sleep(2)

    def geciktirici(attacker, defencer): #regular
        print("{0} used geciktirici, his attack powered and hits twice".format(attacker.title))
        attacker.dickSize += 2
        attacker.attack(defencer, attacker.dickSize)
        time.sleep(1)
        attacker.attack(defencer, attacker.dickSize)
        resetDS(attacker)
        time.sleep(2)

    def dickSlap(attacker, defencer): #regular 
        print("{0} is getting ready for slappin yo ass".format(attacker.title))
        attacker.dickSize += 3
        attacker.attack(defencer, attacker.dickSize)
        resetDS(attacker)
        

    def spankDaddy(attacker, defencer): #regular 
        print("WOOHOO THAT'S HOT. {0} GONNA SPANK YOU HARD".format(attacker.title))
        attacker.dickSize += 4
        attacker.attack(defencer, attacker.dickSize)
        resetDS(attacker)
        

    def assholeVacuum(attacker, defencer): #legendary 
        print("DAMN LOOK AT THAT VACUUM POWER ! ALL OF THIS ONLY WITH MOUTH")
        attacker.dickSize += 48
        attacker.attack(defencer, attacker.dickSize)
        resetDS(attacker)
        
    
    def ReverseCard(attacker, defencer, moveList, moveIndex): #legendary
        move = moveList[moveIndex]
        if move == 'amguard':
            print("REVERSE CARD!\n{0}'s amguard taken back lol".format(defencer.title))
            defencer.assholeArmor -= 80
            Moves.amguard(attacker)
        elif move == 'quadroDick':
            print("REVERSE CARD!\nGOTCHAA, {0}'s DICK DID NOTHINGG".format(defencer.title))
            Moves.quadroDick(attacker)
            armorHpRegulizer(attacker,defencer.dickSize*4)
        elif move == 'kucultucu':
            Moves.kucultucu(defencer)
            print("REVERSE CARD!\nNIGGA {0} PUT THE KUCULTUCU TO {1}'s DICK".format(attacker.title, defencer.title))
        elif move == 'geciktirici':
            print("REVERSE CARD!\nNOPE {0} USED BETTER GECIKTIRICI".format(attacker.title))
            Moves.geciktirici(attacker)
            armorHpRegulizer(attacker,defencer.dickSize+defencer.dickSize)
        elif move == 'ReverseCard':
            newMoveIndex = moveIndex - 1
            Moves.ReverseCard(attacker, defencer, moveList, newMoveIndex)
        elif move == 'invalidMove':
            print('Man last move was invalid you wasted your reverseCard')
        elif move == 'dickSlap':
            print('REVERSE CARD !! THATS HOW YOU SLAP')
            Moves.dickSlap(attacker, defencer)
            armorHpRegulizer(attacker,defencer.dickSize+3)
        elif move == 'spankDaddy':
            print('REVERSE CARD !! RESPANK !')
            Moves.spankDaddy(attacker, defencer)
            armorHpRegulizer(attacker,defencer.dickSize+4)
        elif move == 'assholeVacuum':
            print('REVERSE CARD !! THATS HOW YOU VACCUM BITCHH')
            Moves.assholeVacuum(attacker, defencer)
            armorHpRegulizer(attacker, defencer.dickSize+48)


def armorHpRegulizer(attacker, damage):
    if attacker.assholeArmor > 0:
        attacker.assholeArmor += damage
    else:
        if (attacker.hp + damage) > attacker.defaultHP:
            extraArmor = damage - (attacker.defaultHP - attacker.hp)
            attacker.hp = attacker.defaultHP
            attacker.assholeArmor += extraArmor
        else:
            attacker.hp += damage

def resetDS(attacker):
    attacker.dickSize = attacker.defaultDickSize

def currentCharList():
    CharList = {
        'buyukbabaMax' : ['BuyukbabaMAX', 14, 'BUYUKBABA MAX' ],
        'emanetoglu' : ['EMANETOGLU', 12, "GIRESUNLU ASIRET VARISI"]
    }

    return CharList

def currentMoveList():
    MoveList = {
        'regular' : ['geciktirici', 'dickSlap', 'spankDaddy'],
        'legendary' : ['amguard', 'quadroDick', 'kucultucu', 'assholeVacuum', 'ReverseCard']

    }
    return MoveList

def setAvaliableMoves(roundNumber, regularMoves, legendaryMoves):
    avaliableMoves = {}
    if roundNumber < 4:
        indx1, indx2, indx3 = random.sample(range(0,3),3)
        indx4 = random.randint(0,4)
        avaliableMoves.update({1:regularMoves[indx1]})
        avaliableMoves.update({2:regularMoves[indx2]})
        avaliableMoves.update({3:regularMoves[indx3]})
        avaliableMoves.update({4:legendaryMoves[indx4]})
    else:
        indx1, indx2 = random.sample(range(0,3),2)
        indx3, indx4 = random.sample(range(0,5),2)
        avaliableMoves.update({1:regularMoves[indx1]})
        avaliableMoves.update({2:regularMoves[indx2]})
        avaliableMoves.update({3:legendaryMoves[indx3]})
        avaliableMoves.update({4:legendaryMoves[indx4]})

    return avaliableMoves

        

def AnnounceRoundNumber(number):
    roundNum = 0
    if number % 1 == 0.0 or number % 1 == 0:
        roundNum = int(number)
        print("##################################################################################### ROUND {0} ####################################################################################".format(roundNum))
    else:
        roundNum = int(number)
    return roundNum





# def chooseRandomChar():
#     fp = random.randint(0,1)
#     sp = 0
#     if fp == 1:
#         return fp, sp
#     else:
#         sp = 1
#         return fp, sp

def countDown():
    print("3")
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('Match Begins')
    time.sleep(1)


# i copied this func from stackoverflow -> https://stackoverflow.com/questions/48035367/python-text-game-health-bar
def do_health(health, maxHealth):
    healthDashes=20
    dashConvert = int(maxHealth/healthDashes)                         # Get the number to divide by to convert health to dashes (being 10)
    currentDashes = int(health/dashConvert)                           # Convert health to dash count: 80/10 => 8 dashes
    remainingHealth = healthDashes - currentDashes                    # Get the health remaining to fill as space => 12 spaces

    healthDisplay = ''.join(['-' for i in range(currentDashes)])      # Convert 8 to 8 dashes as a string:   "--------"
    remainingDisplay = ''.join([' ' for i in range(remainingHealth)]) # Convert 12 to 12 spaces as a string: "            "
    percent = str(int((health/maxHealth)*100)) + "%"                  # Get the percent as a whole number:   40%
    
    bar = "|{0}{1}|".format(healthDisplay, remainingDisplay)               # Print out textbased healthbar

    return bar, percent

def do_armor(armor, maxArmor):
    armorDashes=20
    dashConvert = int(maxArmor/armorDashes)                         
    currentDashes = int(armor/dashConvert)                          
    remainingArmor = armorDashes - currentDashes                    

    armorDisplay = ''.join(['-' for i in range(currentDashes)])     
    remainingDisplay = ''.join([' ' for i in range(remainingArmor)]) 
    percent = str(int((armor/maxArmor)*100)) + "%"                  
    
    bar = "|{0}{1}|".format(armorDisplay, remainingDisplay)

    return bar, percent

def healthStatus(firstP, secondP):
    firstP_healthBar, firstP_percent = do_health(firstP.hp, firstP.defaultHP)
    secondP_healthBar, secondP_percent = do_health(secondP.hp, secondP.defaultHP)
    firstP_armorBar, firstP_armorPercent = do_armor(firstP.assholeArmor, firstP.defaultAssholeArmor)
    secondP_armorBar, secondP_armorPercent = do_armor(secondP.assholeArmor, secondP.defaultAssholeArmor)
    print("#################################################### HEALTH AND ARMOR STATUS ####################################################\n#         {0}'s health is {1} - {2} {3} / Armor  is {4} - {5} {6}\n#         {7}'s health is {8} - {9} {10} / Armor is {11} - {12} {13}\n#################################################################################################################################".format(firstP.title, firstP.hp, firstP_healthBar, firstP_percent, firstP.assholeArmor, firstP_armorBar, firstP_armorPercent, secondP.title, secondP.hp, secondP_healthBar, secondP_percent, secondP.assholeArmor, secondP_armorBar, secondP_armorPercent))

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