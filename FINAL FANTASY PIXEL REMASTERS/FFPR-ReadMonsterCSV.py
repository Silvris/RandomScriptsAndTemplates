import csv
import os
import sys

class Monster:
    #all of the values we'd want from the monster csv
    def __init__(self,name,lv,hp,mp,exp,gil,strength,vitality,agility,intelligence,spirit,magic,attack,defense,accuracy,evasion,magic_evasion,critical,luck,weight,IsBoss):
        self.name = name
        self.lvl = lv
        self.hp = hp
        self.mp = mp
        self.exp = exp
        self.gil = gil
        self.strength = strength
        self.vitality = vitality
        self.agility = agility
        self.intelligence = intelligence
        self.spirit = spirit
        self.magic = magic
        self.attack = attack
        self.defense = defense
        self.accuracy = accuracy
        self.evasion = evasion
        self.magic_evasion = magic_evasion
        self.critical = critical
        self.luck = luck
        self.weight = weight
        self.IsBoss = IsBoss

abspath = os.path.abspath(sys.argv[0])

dname = os.path.dirname(abspath)

os.chdir(dname)
monsterData = csv.DictReader(open("monster.csv",'r',encoding='utf-8'),delimiter=",")
monsterNames = csv.DictReader(open("system_en.csv",'r',encoding='utf-8'),delimiter="\t") #you will need to edit this to have Key\tString on the first line
outdata = open("FF1-Monsters.txt",'w')

nameDict = dict()
for row in monsterNames:
    nameDict[row['Key']] = row['String']

monsters = list()
for monster in monsterData:
    monsters.append(Monster(
        nameDict[monster['mes_id_name']],monster['lv'],monster['hp'],monster['mp'],monster['exp'],monster['gill'],
        monster['strength'],monster['vitality'],monster['agility'],monster['intelligence'],monster['spirit'],monster['magic'],
        monster['attack'],monster['defense'],monster['accuracy_rate'],monster['evasion_rate'],monster['magic_evasion_rate'],monster['critical_rate'],monster['luck'],
        monster['weight'],monster['boss']))

for monster in monsters:
    #print(monster.name, monster.IsBoss)
    outdata.write("{}\n".format(monster.name))
    if monster.IsBoss == "1":
        outdata.write("BOSS\n")
    else:
        outdata.write("Monster\n")
    outdata.write("HP:{}\n".format(monster.hp))
    outdata.write("MP:{}\n".format(monster.mp))
    outdata.write("EXP Gained:{}\n".format(monster.exp))
    outdata.write("Gil Dropped:{}\n".format(monster.gil))
    outdata.write("Strength:{}\n".format(monster.strength))
    outdata.write("Vitality:{}\n".format(monster.vitality))
    outdata.write("Agility:{}\n".format(monster.agility))
    outdata.write("Intelligence:{}\n".format(monster.intelligence))
    outdata.write("Spirit:{}\n".format(monster.spirit))
    outdata.write("Magic:{}\n".format(monster.magic))
    outdata.write("Attack:{}\n".format(monster.attack))
    outdata.write("Defense:{}\n".format(monster.defense))
    outdata.write("Accuracy Rate:{}\n".format(monster.accuracy))
    outdata.write("Evasion Rate:{}\n".format(monster.evasion))
    outdata.write("Magic Evasion Rate:{}\n".format(monster.magic_evasion))
    outdata.write("Critical Rate:{}\n".format(monster.critical))
    outdata.write("Luck:{}\n".format(monster.luck))
    outdata.write("Weight:{}\n\n".format(monster.weight))