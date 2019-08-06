import random


class Char:

    title = ''
    damage = ''
    details = ''
    is216 = False
    hp = 100
    armor = 69
    assholeArmor = 50
    assholeSize = 1
    dickSize = 5

    def __init__(self,title, damage, details):
        self.title = title
        self.damage = damage
        self.details = details

    def move(self, Moves):
        return self.dickSize
    
    def attack(self,Char, damage):
        Char.hp -= damage

class Moves:

    def amguard(Char):
        Char.assholeArmor += 20
        print('{0} HAS GAINED 20 ASSHOLE ARMOR'.format(Char.title))
        return 1

    def quadroDick(Char):
        Char.dickSize += 20
        print("{0}'s dick size increased by 20 cm NOW HAS x4 DAMAGE".format(Char.title))
        return 1

    def sedativeDick(Char):
        Char.dickSize = 2
        print("{0}'s dick size decrased to 2 cm DAMN NIGGA MICROPENIS".format(Char.title))
        return 1

    def geciktirici(Char):
        Char.dickSize += 8
        print("{0} used geciktirici, he attack powered and hits twice")
        return 2





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
