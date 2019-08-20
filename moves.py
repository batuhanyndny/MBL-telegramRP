import random
import time


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
        Moves.resetDS(attacker)
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
        Moves.resetDS(attacker)
        time.sleep(2)

    def dickSlap(attacker, defencer): #regular 
        print("{0} is getting ready for slappin yo ass".format(attacker.title))
        attacker.dickSize += 3
        attacker.attack(defencer, attacker.dickSize)
        Moves.resetDS(attacker)
        

    def spankDaddy(attacker, defencer): #regular 
        print("WOOHOO THAT'S HOT. {0} GONNA SPANK YOU HARD".format(attacker.title))
        attacker.dickSize += 4
        attacker.attack(defencer, attacker.dickSize)
        Moves.resetDS(attacker)
        

    def assholeVacuum(attacker, defencer): #legendary 
        print("DAMN LOOK AT THAT VACUUM POWER ! ALL OF THIS ONLY WITH MOUTH")
        attacker.dickSize += 48
        attacker.attack(defencer, attacker.dickSize)
        Moves.resetDS(attacker)

    def tencere(attacker): #outstanding
        print("{0} PUT THE TENCERE TO HIS ASS. NOW HAS 20 ASSHOLE ARMOR".format(attacker.title))
        attacker.assholeArmor += 20
        time.sleep(2)

    def ancientStand(attacker): #outstanding
        print("NOW {0} PERFORMING IN THE ANCINET VIRGIN STAND. HE WILL BLOCK THE NEXT MOVE !".format(attacker.title))
        attacker.hasBlock = True

    def Linc(attacker, defencer): # outstanding
        print("{0} SHOUTS AND GATHERS A GROUP OF COMARS THAT LINCS {1}. {2} GAINED 25 ASSHOLE ARMOR AND DEALS DAMAGE TO {3} BY 30".format(attacker.title, defencer.title, attacker.title, defencer.title))
        attacker.attack(defencer, 30)
        attacker.assholeArmor += 25

    def ReverseCard(attacker, defencer, moveList, moveIndex): #legendary
        move = moveList[moveIndex]
        if move == 'amguard':
            print("REVERSE CARD!\n{0}'s amguard taken back lol".format(defencer.title))
            defencer.assholeArmor -= 80
            Moves.amguard(attacker)
        elif move == 'quadroDick':
            print("REVERSE CARD!\nGOTCHAA, {0}'s DICK DID NOTHINGG".format(defencer.title))
            Moves.quadroDick(attacker, defencer)
            Moves.armorHpRegulizer(attacker,defencer.dickSize*4)
        elif move == 'kucultucu':
            Moves.kucultucu(defencer)
            Moves.resetDS(attacker)
            print("REVERSE CARD!\nNIGGA {0} PUT THE KUCULTUCU TO {1}'s DICK".format(attacker.title, defencer.title))
        elif move == 'geciktirici':
            print("REVERSE CARD!\nNOPE {0} USED BETTER GECIKTIRICI".format(attacker.title))
            Moves.geciktirici(attacker, defencer)
            Moves.armorHpRegulizer(attacker,defencer.dickSize+defencer.dickSize)
        elif move == 'ReverseCard':
            newMoveIndex = moveIndex - 1
            Moves.ReverseCard(attacker, defencer, moveList, newMoveIndex)
        elif move == 'invalidMove':
            print('Man last move was invalid you wasted your reverseCard')
        elif move == 'dickSlap':
            print('REVERSE CARD !! THATS HOW YOU SLAP')
            Moves.dickSlap(attacker, defencer)
            Moves.armorHpRegulizer(attacker,defencer.dickSize+3)
        elif move == 'spankDaddy':
            print('REVERSE CARD !! RESPANK !')
            Moves.spankDaddy(attacker, defencer)
            Moves.armorHpRegulizer(attacker,defencer.dickSize+4)
        elif move == 'assholeVacuum':
            print('REVERSE CARD !! THATS HOW YOU VACCUM BITCHH')
            Moves.assholeVacuum(attacker, defencer)
            Moves.armorHpRegulizer(attacker, defencer.dickSize+48)
        elif move == 'tencere':
            print('REVERSE CARD !! {0} STOLE THE TENCERE'.format(attacker.title))
            Moves.tencere(attacker)
            defencer.assholeArmor -= 20
        elif move == 'ancientStand':
            print("REVERSE CARD !! {0} STOLE THE VIRGIN STAND FROM {1}".format(attacker.title, defencer.title))
            Moves.ancientStand(attacker)
            defencer.hasBlock = False
        elif move == 'Linc':
            print("REVERSE CARD !! {0} SAID TO COMARS THAT {1} IS FEDOCU. NOW {2} IS GETTIN BULLIED".format(attacker.title, defencer.title, defencer.title))
            Moves.Linc(attacker, defencer)
            Moves.armorHpRegulizer(attacker, 30)
            defencer.assholeArmor -= 25

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

    def currentMoveList():
        MoveList = {
        'regular' : {   'geciktirici':'USES GECIKTIRICI TO LAST LONGER. HITS TWICE', 
                        'dickSlap':'SLAP THE ENEMYS ASS WITH YOUR DICK. HITS ONCE', 
                        'spankDaddy':'SPANK THE ENEMY IN THE BUTT. HITS ONCE'},

        'outstanding' : {'tencere':'WRAP TENCERE AROUND YO ASS. GAIN 20 ASSHOLE ARMOR', 
                        'ancientStand':'PERFORM THE ANCIENT VIRGIN STAND. BLOCKS ENEMY ONCE', 
                        'Linc':'GATHER A GROUP OF COMARS AND BULLY THE ENEMY. GAIN 25 ASSHOLE ARMOR AND DEAL 30 DAMAGE'},

        'legendary' : {'amguard':'PUT AMGUARD TO YOUR ASS. GAIN 80 ASSHOLE ARMOR', 
                        'quadroDick':'YOUR DICK IS 4X LONGER. HIT ENEMY HARD', 
                        'kucultucu': 'MAKE YOUR ENEMYS DICK SIZE 2. BEHOLD MICROPENIS', 
                        'assholeVacuum': 'WHAT A MAGIC WITH MOUTH. DEAL +48 DAMAGE', 
                        'ReverseCard': 'PARKOURR'}

        }
        return MoveList