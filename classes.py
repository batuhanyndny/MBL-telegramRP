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

    def amguard(Char):
        Char.assholeArmor += 80
        print('{0} HAS GAINED 80 ASSHOLE ARMOR'.format(Char.title))
        time.sleep(2)


    def quadroDick(Char):
        print("{0}'s dick size increased to {1} cm NOW HAS x4 DAMAGE".format(Char.title, Char.dickSize*4))
        Char.dickSize = Char.dickSize*4
        time.sleep(2)

    def kucultucu(Char):
        Char.dickSize = 2
        print("{0}'s dick size decrased to 2 cm DAMN NIGGA MICROPENIS".format(Char.title))
        time.sleep(2)

    def geciktirici(Char):
        Char.dickSize += 2
        print("{0} used geciktirici, his attack powered and hits twice".format(Char.title))
        time.sleep(2)
    
    def ReverseCard(attacker, defencer, moveList, moveIndex):
        move = moveList[moveIndex]
        if move == 'amguard':
            print("REVERSE CARD!\n{0}'s amguard taken back lol".format(defencer.title))
            defencer.assholeArmor -= 80
            Moves.amguard(attacker)
        elif move == 'quadroDick':
            print("REVERSE CARD!\nGOTCHAA, {0}'s DICK DID NOTHINGG".format(defencer.title))
            Moves.quadroDick(attacker)
            attacker.attack(defencer, attacker.dickSize)
            attacker.dickSize = attacker.defaultDickSize
            if attacker.assholeArmor > 0:
                attacker.assholeArmor += defencer.dickSize*4
            else:
                if (attacker.hp + defencer.dickSize*4) > attacker.defaultHP:
                    extraArmor = defencer.dickSize*4 - (attacker.defaultHP - attacker.hp)
                    attacker.hp = attacker.defaultHP
                    attacker.assholeArmor += extraArmor
                else:
                    attacker.hp += defencer.dickSize*4
        elif move == 'kucultucu':
            Moves.kucultucu(defencer)
            print("REVERSE CARD!\nNIGGA {0} PUT THE KUCULTUCU TO {1}'s DICK".format(attacker.title, defencer.title))
        elif move == 'geciktirici':
            print("REVERSE CARD!\nNOPE {0} USED BETTER GECIKTIRICI".format(attacker.title))
            Moves.geciktirici(attacker)
            attacker.attack(defencer, attacker.dickSize)
            time.sleep(1)
            attacker.attack(defencer, attacker.dickSize)
            attacker.dickSize = attacker.defaultDickSize
            if attacker.assholeArmor > 0:
                attacker.assholeArmor += defencer.dickSize+defencer.dickSize
            else:
                attacker.hp += defencer.dickSize+defencer.dickSize
        elif move == 'ReverseCard':
            newMoveIndex = moveIndex - 1
            Moves.ReverseCard(attacker, defencer, moveList, newMoveIndex)




def currentCharList():
    CharList = {
        'buyukbabaMax' : ['Buyukbaba MAX', 14, 'BUYUKBABA MAX' ],
        'emanetoglu' : ['EMANETOGLU', 12, "GIRESUNLU ASIRET VARISI"]
    }

    return CharList

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