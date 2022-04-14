import csv
import os
import sys

class Monster:
    #all of the values we'd want from the monster csv
    def __init__(self,name,lv,hp,mp,exp,gil,strength,vitality,agility,intelligence,spirit,magic,attack,abilityAttack,defense,abilityDefense,accuracy,evasion,magic_evasion,critical,luck,weight,group,IsBoss,species,resistance_attribute,resistance_condition,attackNum,attackBonus,dropRate,drops,steals,scriptID,rageId):
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
        self.rageID = rageId

abspath = os.path.abspath(sys.argv[0])

dname = os.path.dirname(abspath)

os.chdir(dname)
monsterData = csv.DictReader(open("monster.csv",'r',encoding='utf-8'),delimiter=",")
nameData = csv.DictReader(open("system_en.csv",'r',encoding='utf-8'),delimiter="\t") #you will need to edit this to have Key\tString on the first line
monsterPartyData = csv.DictReader(open("monster_party.csv",'r',encoding='utf-8'),delimiter=",")
monsterSetData = csv.DictReader(open("monster_set.csv",'r',encoding='utf-8'),delimiter=",")
mapData = csv.DictReader(open("map.csv",'r',encoding="utf-8"),delimiter=',')
areaData = csv.DictReader(open("area.csv",'r',encoding='utf-8'),delimiter=",")
outdata = open("FF6-EncounterTables.txt",'w')

nameDict = dict()
for row in nameData:
    nameDict[row['Key']] = row['String']
monsters = dict()
for monster in monsterData:
    if monster["mes_id_name"] != "None":
        if monster["mes_id_name"] in nameDict:
            name = nameDict[monster['mes_id_name']]
        else:
            name = monster["mes_id_name"]
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
    monsters[monster["id"]] = Monster(
        name,
        monster['lv'],
        monster['hp'],
        monster['mp'],
        monster['exp'],
        monster['gill'],
        monster['strength'],
        monster['vitality'],
        monster['agility'],
        monster['intelligence'],
        monster['spirit'],
        monster['magic'],
        monster['attack'],
        monster["ability_attack"],
        monster['defense'],
        monster['ability_defense'],
        monster['accuracy_rate'],
        monster['evasion_rate'],
        monster['magic_evasion_rate'],
        monster['critical_rate'],
        monster['luck'],
        monster['weight'],
        monster["monster_flag_group_id"],
        monster['boss'],
        monster["species"],
        monster["resistance_attribute"],
        monster["resistance_condition"],
        monster["attack_count"],
        monster["attack_plus"],
        monster["drop_rate"],
        drops,
        steals,
        monster["script_id"],
        monster["rage_ability_random_group_id"])
print(len(monsters))
monster_parties = dict()
for party in monsterPartyData:
    partyInfo = ""
    for i in range(1,10):
        if party["monster{}".format(i)] != "0":
            #print(party["monster{}".format(i)])
            monster =  monsters[party["monster{}".format(i)]]
            print(party["monster{}".format(i)],monster.name)
            partyInfo += monster.name
            partyInfo += ", "
    partyInfo = partyInfo[:-2]
    monster_parties[party["id"]] = partyInfo
monster_sets = dict()
for partySet in monsterSetData:
    setInfo = list()
    for i in range(1,17):
        if partySet["monster_set{}_rate".format(i)] != "0" and partySet["monster_set{}".format(i)] != "0":
            setInfo.append([monster_parties[partySet["monster_set{}".format(i)]],partySet["monster_set{}_rate".format(i)]])
    monster_sets[partySet["id"]] = (setInfo)
areas = dict()
for area in areaData:
    if area["area_name"] in nameDict:
        #print(area["area_name"])
        areas[area["id"]] = nameDict[area["area_name"]]
    else:
        areas[area["id"]] = "None"
#print(areas)
for map in mapData:
    #just need to grab name and monster set info
    if(map["monster_set_id"] != "0"):
        #print(int(map["monster_set_id"]))
        areaName = areas[map["area_id"]]
        if map["map_title"] in nameDict:
            mapName = " - " + nameDict[map["map_title"]]
        else:
            mapName = ""
        mapSet = monster_sets[map["monster_set_id"]]
        outdata.write("{}{}:\n".format(areaName,mapName))
        for encounter in mapSet:
            #print(map["monster_set_id"],encounter)
            outdata.write("{group}: {rate}\n".format(group=encounter[0],rate=encounter[1]))
        outdata.write("\n")
