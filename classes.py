import random
import time

class Char:

    title = ''
    damage = ''
    details = ''
    is216 = False
    hp = 420
    assholeArmor = 69
    assholeSize = 1
    dickSize = 7

    hasBlock = False

    defaultDickSize = 7
    defaultHP = 420
    

    def __init__(self,title, damage, details):
        self.title = title
        self.damage = damage
        self.details = details

    
    def attack(self,Char, damage):
        if Char.hasBlock:
            print("NAH MAN YOUR ATTACK JUST GET BLOCKED")
        else:
            if Char.assholeArmor != 0:
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

    def amguard(Char):
        Char.assholeArmor += 20
        print('{0} HAS GAINED 20 ASSHOLE ARMOR'.format(Char.title))
        time.sleep(2)


    def quadroDick(Char):
        Char.dickSize += Char.dickSize*4
        print("{0}'s dick size increased by {1} cm NOW HAS x4 DAMAGE".format(Char.title, Char.dickSize*4))
        time.sleep(2)

    def sedativeDick(Char):
        Char.dickSize = 2
        print("{0}'s dick size decrased to 2 cm DAMN NIGGA MICROPENIS".format(Char.title))
        time.sleep(2)

    def geciktirici(Char):
        Char.dickSize += 2
        print("{0} used geciktirici, his attack powered and hits twice")
        time.sleep(2)




def currentCharList():
    CharList = {
        'buyukbabaMax' : ['Buyukbaba MAX', 23, 'BUYUKBABA MAX' ],
        'emanetoglu' : ['EMANETOGLU', 27, "GIRESUNLU ASIRET VARISI"]
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