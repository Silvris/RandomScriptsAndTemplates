import csv
import os
import sys

class Monster:
    #all of the values we'd want from the monster csv
    def __init__(self,name,lv,hp,mp,exp,gil,strength,vitality,agility,intelligence,spirit,magic,attack,abilityAttack,defense,abilityDefense,accuracy,evasion,magic_evasion,critical,luck,weight,group,IsBoss,species,resistance_attribute,resistance_condition,attackNum,attackBonus,dropRate,drops,steals,scriptID):
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
        self.abilityAttack = abilityAttack
        self.defense = defense
        self.abilityDefense = abilityDefense
        self.accuracy = accuracy
        self.evasion = evasion
        self.magic_evasion = magic_evasion
        self.critical = critical
        self.luck = luck
        self.weight = weight
        self.group = group
        self.IsBoss = IsBoss
        self.species = species
        self.resistance_attribute = resistance_attribute
        self.resistance_condition = resistance_condition
        self.attackNum = attackNum
        self.attackBonus = attackBonus
        self.dropRate = dropRate
        self.drops = drops
        self.steals = steals
        self.scriptID = scriptID

abspath = os.path.abspath(sys.argv[0])

dname = os.path.dirname(abspath)

os.chdir(dname)
monsterData = csv.DictReader(open("monster.csv",'r',encoding='utf-8'),delimiter=",")
itemData = csv.DictReader(open("content.csv",'r',encoding='utf-8'),delimiter=",")
monsterNames = csv.DictReader(open("system_en.csv",'r',encoding='utf-8'),delimiter="\t") #you will need to edit this to have Key\tString on the first line
outdata = open("FF5-Monsters.txt",'w')

nameDict = dict()
for row in monsterNames:
    nameDict[row['Key']] = row['String']
itemList = list()
for item in itemData:
    itemList.append(item)
monsters = list()
for monster in monsterData:
    if monster["mes_id_name"] != "None":
        name = nameDict[monster['mes_id_name']]
    else:
        name = "None"
    drops = list()
    steals = list()
    for i in range(8):
        drops.append([
            monster["drop_content_id{}".format(i+1)],
            monster["drop_content_id{}_value".format(i+1)]
        ])
    for i in range(4):
        steals.append(
            monster["steal_content_id{}".format(i+1)]
        )
    monsters.append(Monster(
        name,monster['lv'],monster['hp'],monster['mp'],monster['exp'],monster['gill'],
        monster['strength'],monster['vitality'],monster['agility'],monster['intelligence'],monster['spirit'],monster['magic'],
        monster['attack'],monster["ability_attack"],monster['defense'],monster['ability_defense'],monster['accuracy_rate'],monster['evasion_rate'],monster['magic_evasion_rate'],monster['critical_rate'],monster['luck'],
        monster['weight'],monster["monster_flag_group_id"],monster['boss'],monster["species"],monster["resistance_attribute"],monster["resistance_condition"],monster["attack_count"],monster["attack_plus"],monster["drop_rate"],drops,steals,monster["script_id"]))

for monster in monsters:
    #print(monster.name, monster.IsBoss)
    outdata.write("{}\n".format(monster.name))
    outdata.write("Species:{}\n".format(monster.species))
    if monster.IsBoss == "1":
        outdata.write("BOSS\n")
    else:
        outdata.write("Monster\n")
    outdata.write("Group:{}\n".format(monster.group))
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
    outdata.write("Ability Attack:{}\n".format(monster.abilityAttack))
    outdata.write("Ability Defense:{}\n".format(monster.abilityDefense))
    outdata.write("Accuracy Rate:{}\n".format(monster.accuracy))
    outdata.write("Evasion Rate:{}\n".format(monster.evasion))
    outdata.write("Magic Evasion Rate:{}\n".format(monster.magic_evasion))
    outdata.write("Critical Rate:{}\n".format(monster.critical))
    outdata.write("Luck:{}\n".format(monster.luck))
    outdata.write("Resistance Attribute:{}\n".format(monster.resistance_attribute))
    outdata.write("Resistance Condition:{}\n".format(monster.resistance_condition))
    outdata.write("Drop Rate:{}\n".format(monster.dropRate))
    outdata.write("Drops:\n")
    dropIndex = 1
    for drop in monster.drops:
        #print(drop[0])

        itemDef = next((item for item in itemList if item["id"] == drop[0]),None)
        if itemDef != None:
            itemName = nameDict[itemDef["mes_id_name"]]
            outdata.write("{} {}\n".format(drop[1],itemName[itemName.find(">")+1:]))
        else:
            if dropIndex == 1:
                outdata.write("None\n")
        dropIndex +=1
    stealIndex = 1
    outdata.write("Steals:\n")
    for steal in monster.steals:
        itemDef = next((item for item in itemList if item["id"] == steal),None)
        if itemDef != None:
            itemName = nameDict[itemDef["mes_id_name"]]
            outdata.write("{}\n".format(itemName[itemName.find(">")+1:]))
        else:
            if stealIndex == 1:
                outdata.write("None\n")
        stealIndex +=1
    outdata.write("Weight:{}\n".format(monster.weight))
    outdata.write("Script ID:{}\n\n".format(monster.scriptID))