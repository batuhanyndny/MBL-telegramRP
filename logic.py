import random
import time


def setAvaliableMoves(roundNumber, currentMoveList):
    avaliableMoves = {}
    regMoves = currentMoveList['regular']
    outsMoves = currentMoveList['outstanding']
    legMoves = currentMoveList['legendary']
    if roundNumber < 4:
        indx1, indx2, indx3 = random.sample(range(0, 3), 3)
        indx4 = random.sample(range(0, 3), 1)[0]

        avaliableMoves.update({1: [list(regMoves.keys())[indx1], regMoves[list(regMoves.keys())[indx1]]]})
        avaliableMoves.update({2: [list(regMoves.keys())[indx2], regMoves[list(regMoves.keys())[indx2]]]})
        avaliableMoves.update({3: [list(regMoves.keys())[indx3], regMoves[list(regMoves.keys())[indx3]]]})
        avaliableMoves.update({4: [list(outsMoves.keys())[indx4], outsMoves[list(outsMoves.keys())[indx4]]]})
    else:
        indx1, indx2 = random.sample(range(0, 3), 2)
        indx3, indx4 = random.sample(range(0, 5), 2)

        avaliableMoves.update({1: [list(outsMoves.keys())[indx1], outsMoves[list(outsMoves.keys())[indx1]]]})
        avaliableMoves.update({2: [list(outsMoves.keys())[indx2], outsMoves[list(outsMoves.keys())[indx2]]]})
        avaliableMoves.update({3: [list(legMoves.keys())[indx3], legMoves[list(legMoves.keys())[indx3]]]})
        avaliableMoves.update({4: [list(legMoves.keys())[indx4], legMoves[list(legMoves.keys())[indx4]]]})

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
    healthDashes = 20
    dashConvert = int(maxHealth / healthDashes)                         # Get the number to divide by to convert health to dashes (being 10)
    currentDashes = int(health / dashConvert)                           # Convert health to dash count: 80/10 => 8 dashes
    remainingHealth = healthDashes - currentDashes                    # Get the health remaining to fill as space => 12 spaces

    healthDisplay = ''.join(['-' for i in range(currentDashes)])      # Convert 8 to 8 dashes as a string:   "--------"
    remainingDisplay = ''.join([' ' for i in range(remainingHealth)])  # Convert 12 to 12 spaces as a string: "            "
    percent = str(int((health / maxHealth) * 100)) + "%"                  # Get the percent as a whole number:   40%

    bar = "|{0}{1}|".format(healthDisplay, remainingDisplay)               # Print out textbased healthbar

    return bar, percent


def do_armor(armor, maxArmor):
    armorDashes = 20
    dashConvert = int(maxArmor / armorDashes)
    currentDashes = int(armor / dashConvert)
    remainingArmor = armorDashes - currentDashes

    armorDisplay = ''.join(['-' for i in range(currentDashes)])
    remainingDisplay = ''.join([' ' for i in range(remainingArmor)])
    percent = str(int((armor / maxArmor) * 100)) + "%"

    bar = "|{0}{1}|".format(armorDisplay, remainingDisplay)

    return bar, percent


def healthStatus(firstP, secondP):
    firstP_healthBar, firstP_percent = do_health(firstP.hp, firstP.defaultHP)
    secondP_healthBar, secondP_percent = do_health(secondP.hp, secondP.defaultHP)
    firstP_armorBar, firstP_armorPercent = do_armor(firstP.assholeArmor, firstP.defaultAssholeArmor)
    secondP_armorBar, secondP_armorPercent = do_armor(secondP.assholeArmor, secondP.defaultAssholeArmor)
    print("#################################################### HEALTH AND ARMOR STATUS ####################################################\n#         {0}'s health is {1} - {2} {3} / Armor  is {4} - {5} {6}\n#         {7}'s health is {8} - {9} {10} / Armor is {11} - {12} {13}\n#################################################################################################################################".format(
        firstP.title, firstP.hp, firstP_healthBar, firstP_percent, firstP.assholeArmor, firstP_armorBar, firstP_armorPercent, secondP.title, secondP.hp, secondP_healthBar, secondP_percent, secondP.assholeArmor, secondP_armorBar, secondP_armorPercent))


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
