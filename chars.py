
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
            Char.hasBlock = False
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

    def currentCharList():
        CharList = {
        'buyukbabaMax' : ['BuyukbabaMAX', 14, 'BUYUKBABA MAX' ],
        'emanetoglu' : ['EMANETOGLU', 12, "GIRESUNLU ASIRET VARISI"]
        }

        return CharList
