import struct
import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def readInt(file):
    #print(file.tell())
    return struct.unpack("i",file.read(4))[0]

def readUInt(file):
    #print(file.tell())
    return struct.unpack("I",file.read(4))[0]

def readFloat(file):
    return struct.unpack("f",file.read(4))[0]

#on further realization, why the hell does this work
#python, why are you maintaining order in a dict?

DataName = {
    "Index":True,
    "Variation":True,
    "BaseLif":True,
    "BasePow":True,
    "BaseInt":True,
    "BaseSki":True,
    "BaseSpd":True,
    "BaseDef":True,
    "LifGain":True,
    "PowGain":True,
    "IntGain":True,
    "SkiGain":True,
    "SpdGain":True,
    "DefGain":True,
    "ForwardMov":False,
    "BackwardsMov":False,
    "GutsRcvr":True,
    "Lifespan":True
}
for i in range(3,22):
    DataName["Unkn{}".format(i)] = True

MainSubName  = {
    "Index":True,
    "Name":False,
    "Unkn1":True,
    "Unkn2":True,
    "LifeType":True
}

for i in range(3,22):
    MainSubName["Unkn{}".format(i)] = True

TechName = {
    "Index":True,
    "Name":False,
    "Unkn1":True,
    "Unkn2":True,
    "Range":True,
    "GutsCost":True,
    "Force":True,
    "Unkn3":True,
    "Hit":True,
    "Withering":True,
    "Critical":True,
    "Unkn4":True
}

TechLearningName = {
    "Index":True,
    "MainBreed":True,
    "SpecificMainSub":True,
    "ExcludeMainSub":True,
    "Unkn1":True,
    "TechIndex":True,
    "Unkn2":True,
    "Unkn3":True,
    "RequiredStat":True,
    "RequiredNumerical":True,
    "Unkn4":True,
    "Unkn5":True
}

ItemName = {
    "Index":False,
    "Name":True,
    "Description":True,
    "EffectIndex":True,
    "EffectTable":False,
    "BuyPrice":False,
    "SalePrice":False,
    "SellPrice":False,
    "Unkn1":False,
    "Unkn2":False,
    "Unkn3":False,
    "Unkn4":False,
    "Unkn5":False
}

ConsumableName = {
    "Index":True,
    "Unkn1":True,
    "Unkn2":True,
    "Unkn3":True,
    "Unkn4":True,
    "Unkn5":True,
    "Unkn6":True,
    "Unkn7":True,
    "Unkn8":True,
    "Unkn9":True,
    "Unkn10":True,
    "Unkn11":True,
    "Unkn12":True,
    "Unkn13":True,
    "Unkn14":True,
    "Unkn15":True,
    "Lifespan":True,
    "Unkn16":True, #percent lifespan?
    "Dependency":True,
    "PercentDependency":True,
    "Fear":True,
    "PercentFear":True,
    "Unkn19":True,
    "Unkn20":True,
    "Fatigue":True,
    "PercentFatigue":True,
    "Stress":True,
    "PercentStress":True, #Stress
    "Weight":True,
    "PercentWeight":True,
    "Anger":True,
    "PercentAnger":True,
    "Life":True,
    "Power":True,
    "Intelligence":True,
    "Skill":True,
    "Speed":True,
    "Defense":True,
    "Unkn26":True
}

BaseFoodName = {
    "ItemIndex":True,
    "DescriptionHash":False,
    "PurchasePrice":True,
    "CanPurchase":True,
    "FeastItem1":True,
    "FeastItem1Num":True,
    "FeastItem2":True,
    "FeastItem2Num":True,
    "FeastItem3":True,
    "FeastItem3Num":True,
    "Dependence":True,
    "Fear":True,
    "Unkn11":True,
    "Weight":True,
    "Unkn13":True,
    "Unkn14":True
}

SpiceName = {
    "ItemIndex":True,
    "DescriptionHash":False,
    "Fatigue":True,
    "Unkn3":True,
    "Anger":True,
    "Unkn5":True
}

MealName = {
    "Index":True,
    "Name":False,
    "BaseFood":True,
    "Spice":True,
    "Attribute1":True,
    "Attribute2":True,
    "Attribute3":True
}

MonthlyName = {
    "ItemIndex":True,
    "StartMonth":True,
    "EndMonth":True,
    "Unkn1":True,
    "Unkn2":True,
    "Dependency":True,
    "PercentDependency":True,
    "Fear":True,
    "PercentFear":True,
    "Unkn3":True,
    "Unkn4":True,
    "Fatigue":True,
    "PercentFatigue":True,
    "Stress":True,
    "PercentStress":True, #Stress
    "Weight":True,
    "PercentWeight":True,
    "Anger":True,
    "PercentAnger":True,
}

PersonalityName = {
    "Name":False,
    "Unkn1":True,
    "Unkn2":True,
    "Unkn3":True,
    "Unkn4":True,
    "Unkn5":True,
    "Unkn6":True,
    "Unkn7":True,
    "Unkn8":True,
    "Unkn9":True,
    "Unkn10":True
}

TrainerName = {
    "Name":False,
    "Description":False,
    "Price":True,
    "Unkn1":True,
    "PreferredStat":True,
    "Unkn2":True,
    "Index":True,
    "Unkn3":True,
    "Unkn4":True,
    "Unkn5":True,
    "Unkn6":True
}

MainBreedName = {
    "Name":False,
    "Unkn1":True,
    "Unkn2":True,
    "Unkn3":True,
    "Unkn4":True,
    "Unkn5":True,
    "Unkn6":True,
    "Unkn7":True,
    "Unkn8":True
}

FusionItemName = {
    "ItemID":True,
    "FusionResult":True,
    "ResultingMonster":True,
    "RequireMon1":True,
    "RequireMon2":True,
    "RequireMon3":True,
    "RequireMon4":True,
    "FavoredDrill":True,
    "Lifespan":True,
    "Dependence":True,
    "Fear":True,
    "Fame":True,
    "Life":True,
    "Power":True,
    "Intelligence":True,
    "Skill":True,
    "Speed":True,
    "Defense":True,
    "UnlockRequirement":True
}

UnknVariantName = {
    "Index":True,
    "Unkn1":True,
    "Unkn2":True
}

DrillsName = {
    "Name":False,
    "Description":False,
    "Unkn1":True,
    "Unkn2":True,
    "Unkn3":True,
    "Unkn4":True,
    "Unkn5":True,
    "Unkn6":True,
    "Unkn7":True,
    "Unkn8":True,
    "Unkn9":True,
    "Unkn10":True,
    "Unkn11":True,
    "Unkn12":True,
    "Unkn13":True,
    "Unkn14":True,
    "Unkn15":True,
    "Unkn16":True,
    "Unkn17":True,
    "Unkn18":True,
    "Unkn19":True,
    "Unkn20":True,
    "Unkn21":True,
    "Unkn22":True,
    "Unkn23":True
}

PersonalityGroupNames = {
    "Index":False
}

TraitNames = {
    "Index":False,
    "TraitName":False,
    "RearingTrait":True,
    "BattleTrait":True,
    "MonsterName":False,
    "Unkn1":True,
    "Unkn2":True
}

RearingNames = {
    "Index":False,
    "Description":False,
    "UnknString":False,
    "Action":True,
    "Stat":True,
    "Unkn1":True,
    "ActiveValue":True,
    "Unkn2":True,
    "Unkn3":True,
    "Unkn4":True
}

BattleNames = {
    "Index":False,
    "Description":False,
    "UnknString":False,
}

CookieNames = {
    "Name":False,
    "Index":True,
    "Life":True,
    "Power":True,
    "Intelligence":True,
    "Skill":True,
    "Speed":True,
    "Defense":True
}

TournamentNames = {
    "Name":False,
    "Description":False,
    "Rank":True,
    "Month":True,
    "Week":True,
    "Unkn4":True,
    "Unkn5":True,
    "TournamentType":True,#0 - RR, 1 - SingleElim, 2 - Team Battle, 3 - Single Battle
    "Unkn7":True,
    "ParticipantNum":True,
    "Unkn9":True,#time?
    "Unkn10":True,#location
    "Unkn11":True,#fame?
    "RewardFirst":True,
    "RewardRepeat":True,
    "PrizeMoney":True,
    "Unkn15":True,
    "Unkn16":True,
    "Unkn17":True,
    "MinimumAge":True,
    "MaximumAge":True,
    "Unkn20":True,#player slot?
    "Opponent1":True,
    "Opponent2":True,
    "Opponent3":True,
    "Opponent4":True,
    "Opponent5":True,
    "Opponent6":True,
    "Opponent7":True,
    "Opponent8":True,
    "Opponent9":True,
    "Opponent10":True,
    "Opponent11":True,
    "Opponent12":True,
    "Rival1":True,#rival breeder?
    "Rival2":True,#rival monster?
    "Unkn35":True,
    "Unkn36":True,
    "Unkn37":True
}

EnemyMonsterNames ={
    "Index":False,
    "Name":False,#UIString 56
    "HollysMessage":False,
    "MainSub":True,
    "Age":True, #Confirm????
    "Life":True,
    "Power":True,
    "Intelligence":True,
    "Skill":True,
    "Speed":True,
    "Defense":True,
    "ForwardMoveSpeed":True,
    "Backwards":True,
    "GutsRecovery":True,
    "Dependence":True,# 0 to 100 definitely monster parameter
    "Fear":True,# 0 to 100
    "Fame":True,# 0 to 99
    "Trait1":True,
    "Trait2":True,
    "Trait3":True,
    "Trait4":True,
    "Tech1":True,
    "Tech2":True,
    "Tech3":True,
    "Tech4":True,
    "Tech5":True,
    "Tech6":True,
    "Tech7":True,
    "Tech8":True,
    "Tech9":True,
    "Anger":True,
    "Personality":True,
    "Personality2":True
}

for i in range(4,22):
    TechName["Unkn{}".format(i)] = True

for i in range(5,15):
    MonthlyName["Unkn{}".format(i)] = True

for i in range(0,33):
    PersonalityGroupNames["Unkn{}".format(i)] = True

for i in range(2,26):
    BattleNames["Unkn{}".format(i)] = True

def GenerateRemap():
    p2 = csv.DictReader(open("NameRemapP2.csv",'r',newline=''))
    part2 = dict()
    for row in p2:
        part2[row["Name"]] = row["Index"]
    return part2

def ReadItemData(f,remap):
    items = list()
    itemNum = readInt(f)
    for i in range(itemNum):
        item = dict()
        item["Index"] = i
        for field in ItemName:
            if field != "Index":
                datatype = f.read(1)
                #branch on known datatypes
                #print(datatype)
                if datatype == b"\x00":
                    if ItemName[field] == True:
                        item[field] = readUInt(f)
                    else:
                        item[field] = readInt(f)
                elif datatype == b"\x01":
                    item[field] = round(readFloat(f),1)
                else:
                    return item
        #print("EffectIndex:{}".format(item["EffectIndex"]))
        if item["EffectIndex"] in remap:
            item["EffectIndex"] = remap[item["EffectIndex"]]
        items.append(item)
    return items

def ReadItemRemapData(f):
    items = dict()
    itemNum = readInt(f)
    for i in range(itemNum):
        item = dict()
        for field in ["EffectIndex","RemappedIndex"]:
                datatype = f.read(1)
                #branch on known datatypes
                #print(datatype)
                if datatype == b"\x00":
                    item[field] = readInt(f)
                elif datatype == b"\x01":
                    item[field] = round(readFloat(f),1)
                else:
                    return items
        items[item["EffectIndex"]] = item["RemappedIndex"]
    return items

def ReadSingleNullUniString(f, size, offset):
    #Koei Tecmo why
    #print("Offset:{}".format(offset))
    #print("Size:{}".format(size))
    f.seek(offset)
    byteData = f.read(size-1)
    #print(byteData)
    return byteData.decode("utf-16-le")

def ReadJPSingleNullUniString(f, size, offset):
    #Koei Tecmo why
    #print("Offset:{}".format(offset))
    #print("Size:{}".format(size))
    f.seek(offset)
    byteData = f.read(size-1)
    #print(byteData)
    return byteData.decode("shift-jis")

def ReadJPNames(strFile, intFile):
    names = list()
    strCnt = readUInt(strFile)
    intCnt = readUInt(intFile)
    assert strCnt == intCnt
    #get the counts of strings first, since they're easy
    stringInd = list()
    totalName = 0
    for i in range(strCnt):
        value = readInt(strFile)
        stringInd.append(value)
        if value >= 0:
            totalName += 1
    stringOffs = list()
    #print(totalName)
    for i in range(totalName):
        stringOffs.append({
            "offset":readUInt(strFile),
            "size":readUInt(strFile)
        })
    strings = list()
    stringOffset = strFile.tell()
    for i in range(strCnt):
        if stringInd[i] != -1:
            #print(stringInd[i])
            data = stringOffs[stringInd[i]]
            strings.append(ReadJPSingleNullUniString(strFile,data["size"],stringOffset+data["offset"]))
        else:
            strings.append("")
    #now quickly get the list of uints
    ints = list()
    for i in range(intCnt):
        datatype = intFile.read(1)
        if datatype == b"\x00":
            ints.append(readUInt(intFile))
        else:
            ints.append(-1)
    #now bring it together
    for i in range(strCnt):
        names.append({
            "Key":ints[i],
            "Value":strings[i]
        })
    return names

def ReadENNames(strFile, intFile):
    names = list()
    strCnt = readUInt(strFile)
    intCnt = readUInt(intFile)
    assert strCnt == intCnt
    #get the counts of strings first, since they're easy
    stringInd = list()
    totalName = 0
    for i in range(strCnt):
        value = readInt(strFile)
        stringInd.append(value)
        if value >= 0:
            totalName += 1
    stringOffs = list()
    #print(totalName)
    for i in range(totalName):
        stringOffs.append({
            "offset":readUInt(strFile),
            "size":readUInt(strFile)
        })
    strings = list()
    stringOffset = strFile.tell()
    for i in range(strCnt):
        if stringInd[i] != -1:
            #print(stringInd[i])
            data = stringOffs[stringInd[i]]
            strings.append(ReadSingleNullUniString(strFile,data["size"],stringOffset+data["offset"]))
        else:
            strings.append("")
    #now quickly get the list of uints
    ints = list()
    for i in range(intCnt):
        datatype = intFile.read(1)
        if datatype == b"\x00":
            ints.append(readUInt(intFile))
        else:
            ints.append(-1)
    #now bring it together
    for i in range(strCnt):
        names.append({
            "Key":ints[i],
            "Value":strings[i].replace("\n"," ").replace("\r","")
        })
    return names

def ReadGenericData(f,names,IncludeInd = True):
    vals = list()
    valNum = readInt(f)
    for i in range(valNum):
        val = dict()
        if IncludeInd:
            val["Index"] = i
        for field in names:
            if field == "Index" and IncludeInd:
                continue
            else:
                datatype = f.read(1)
                #branch on known datatypes
                #print(datatype)
                if datatype == b"\x00":
                    if names[field] == True:
                        val[field] = readInt(f)
                    else:
                        val[field] = readUInt(f)
                elif datatype == b"\x01":
                    val[field] = round(readFloat(f),1)
                else:
                    return vals
        vals.append(val)
    return vals

def WriteData(f, monsters):
    for monster in monsters:
        f.writerow(monster)


def MainFunction():

    tournamentStrFile = open(r"D:\UKMR\RomFS\string\UIString_EN-decomp\54.bin",'rb')
    tournamentIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\54.bin",'rb')
    tournamentnames = ReadENNames(tournamentStrFile,tournamentIntFile)
    tournamentnamescsv = csv.DictWriter(open("UKMR-TournamentNames.csv",'w',newline='',encoding='utf-8'),["Key","Value"])
    tournamentnamescsv.writeheader()
    WriteData(tournamentnamescsv,tournamentnames)

    tmonsterStrFile = open(r"D:\UKMR\RomFS\string\UIString_EN-decomp\56.bin",'rb')
    tmonsterIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\56.bin",'rb')
    tmonsternames = ReadENNames(tmonsterStrFile,tmonsterIntFile)
    tmonsternamescsv = csv.DictWriter(open("UKMR-EnemyMonsterNames.csv",'w',newline='',encoding='utf-8'),["Key","Value"])
    tmonsternamescsv.writeheader()
    WriteData(tmonsternamescsv,tmonsternames)

    tournamentFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\58.bin",'rb')
    tournament = ReadGenericData(tournamentFile,TournamentNames,False)
    tournamentcsv = csv.DictWriter(open("UKMR-TournamentData.csv",'w',newline=''),TournamentNames)
    tournamentcsv.writeheader()
    WriteData(tournamentcsv,tournament)

    tmonsterFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\59.bin",'rb')
    tmonster = ReadGenericData(tmonsterFile,EnemyMonsterNames,True)
    tmonstercsv = csv.DictWriter(open("UKMR-EnemyMonsterData.csv",'w',newline=''),EnemyMonsterNames)
    tmonstercsv.writeheader()
    WriteData(tmonstercsv,tmonster)

    traitsFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\9.bin",'rb')
    traits = ReadGenericData(traitsFile,TraitNames,True)
    traitscsv = csv.DictWriter(open("UKMR-TraitData.csv",'w',newline=''),TraitNames)
    traitscsv.writeheader()
    WriteData(traitscsv,traits)

    rearingFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\10.bin",'rb')
    rearing = ReadGenericData(rearingFile,RearingNames,True)
    rearingcsv = csv.DictWriter(open("UKMR-RearingTraitData.csv",'w',newline=''),RearingNames)
    rearingcsv.writeheader()
    WriteData(rearingcsv,rearing)

    battletraitsFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\11.bin",'rb')
    battletraits = ReadGenericData(battletraitsFile,BattleNames,True)
    battletraitscsv = csv.DictWriter(open("UKMR-BattleTraitData.csv",'w',newline=''),BattleNames)
    battletraitscsv.writeheader()
    WriteData(battletraitscsv,battletraits)

    cookieFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\16.bin",'rb')
    cookie = ReadGenericData(cookieFile,CookieNames,False)
    cookiecsv = csv.DictWriter(open("UKMR-CookieData.csv",'w',newline=''),CookieNames)
    cookiecsv.writeheader()
    WriteData(cookiecsv,cookie)

    traitsMStrFile = open(r"D:\UKMR\RomFS\string\UIString_EN-decomp\31.bin",'rb')
    traitsMIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\31.bin",'rb')
    traitsMnames = ReadENNames(traitsMStrFile,traitsMIntFile)
    traitsMnamescsv = csv.DictWriter(open("UKMR-TraitMonsterNames.csv",'w',newline='',encoding='utf-8'),["Key","Value"])
    traitsMnamescsv.writeheader()
    WriteData(traitsMnamescsv,traitsMnames)

    traitsStrFile = open(r"D:\UKMR\RomFS\string\UIString_EN-decomp\18.bin",'rb')
    traitsIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\18.bin",'rb')
    traitsnames = ReadENNames(traitsStrFile,traitsIntFile)
    traitsnamescsv = csv.DictWriter(open("UKMR-TraitNames.csv",'w',newline='',encoding='utf-8'),["Key","Value"])
    traitsnamescsv.writeheader()
    WriteData(traitsnamescsv,traitsnames)

    traitsDStrFile = open(r"D:\UKMR\RomFS\string\UIString_EN-decomp\19.bin",'rb')
    traitsDIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\19.bin",'rb')
    traitsDnames = ReadENNames(traitsDStrFile,traitsDIntFile)
    traitsDnamescsv = csv.DictWriter(open("UKMR-RearingTraitDescriptions.csv",'w',newline='',encoding='utf-8'),["Key","Value"])
    traitsDnamescsv.writeheader()
    WriteData(traitsDnamescsv,traitsDnames)

    traitsBStrFile = open(r"D:\UKMR\RomFS\string\UIString_EN-decomp\21.bin",'rb')
    traitsBIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\21.bin",'rb')
    traitsBnames = ReadENNames(traitsBStrFile,traitsBIntFile)
    traitsBnamescsv = csv.DictWriter(open("UKMR-BattleTraitDescriptions.csv",'w',newline='',encoding='utf-8'),["Key","Value"])
    traitsBnamescsv.writeheader()
    WriteData(traitsBnamescsv,traitsBnames)

    pgFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\6.bin",'rb')
    pg = ReadGenericData(pgFile,PersonalityGroupNames,True)
    pgcsv = csv.DictWriter(open("UKMR-PersonalityGroupData.csv",'w',newline=''),PersonalityGroupNames)
    pgcsv.writeheader()
    WriteData(pgcsv,pg)

    pgFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\6.bin",'rb')
    pg = ReadGenericData(pgFile,PersonalityGroupNames,True)
    pgcsv = csv.DictWriter(open("UKMR-PersonalityGroupData.csv",'w',newline=''),PersonalityGroupNames)
    pgcsv.writeheader()
    WriteData(pgcsv,pg)

    pgFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\6.bin",'rb')
    pg = ReadGenericData(pgFile,PersonalityGroupNames,True)
    pgcsv = csv.DictWriter(open("UKMR-PersonalityGroupData.csv",'w',newline=''),PersonalityGroupNames)
    pgcsv.writeheader()
    WriteData(pgcsv,pg)

    drillStrFile = open(r"D:\UKMR\RomFS\string\UIString_EN-decomp\50.bin",'rb')
    drillIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\50.bin",'rb')
    drillnames = ReadENNames(drillStrFile,drillIntFile)
    drillnamescsv = csv.DictWriter(open("UKMR-DrillNames.csv",'w',newline=''),["Key","Value"])
    drillnamescsv.writeheader()
    WriteData(drillnamescsv,drillnames)

    drillFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\46.bin",'rb')
    drill = ReadGenericData(drillFile,DrillsName,False)
    drillcsv = csv.DictWriter(open("UKMR-DrillData.csv",'w',newline=''),DrillsName)
    drillcsv.writeheader()
    WriteData(drillcsv,drill)

    unknVariantFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\65.bin",'rb')
    unknVariant = ReadGenericData(unknVariantFile,UnknVariantName,False)
    unknVariantcsv = csv.DictWriter(open("UKMR-UnknVariantData.csv",'w',newline=''),UnknVariantName)
    unknVariantcsv.writeheader()
    WriteData(unknVariantcsv,unknVariant)

    unknVariant2File = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\66.bin",'rb')
    unknVariant2 = ReadGenericData(unknVariant2File,UnknVariantName,False)
    unknVariant2csv = csv.DictWriter(open("UKMR-UnknVariant2Data.csv",'w',newline=''),UnknVariantName)
    unknVariant2csv.writeheader()
    WriteData(unknVariant2csv,unknVariant2)

    fusionItemFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\36.bin",'rb')
    fusionItem = ReadGenericData(fusionItemFile,FusionItemName,False)
    fusionItemcsv = csv.DictWriter(open("UKMR-FusionItemData.csv",'w',newline=''),FusionItemName)
    fusionItemcsv.writeheader()
    WriteData(fusionItemcsv,fusionItem)

    mbStrFile = open(r"D:\UKMR\RomFS\string\UIString_EN-decomp\14.bin",'rb')
    mbIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\14.bin",'rb')
    mbnames = ReadENNames(mbStrFile,mbIntFile)
    mbnamescsv = csv.DictWriter(open("UKMR-MainBreedNames.csv",'w',newline=''),["Key","Value"])
    mbnamescsv.writeheader()
    WriteData(mbnamescsv,mbnames)

    mbFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\4.bin",'rb')
    mainbreed = ReadGenericData(mbFile,MainBreedName,False)
    mainbreedcsv = csv.DictWriter(open("UKMR-MainBreedData.csv",'w',newline=''),MainBreedName)
    mainbreedcsv.writeheader()
    WriteData(mainbreedcsv,mainbreed)

    trainerStrFile = open(r"D:\UKMR\RomFS\string\UIString_EN-decomp\51.bin",'rb')
    trainerIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\51.bin",'rb')
    trainernames = ReadENNames(trainerStrFile,trainerIntFile)
    trainernamescsv = csv.DictWriter(open("UKMR-TrainerNames.csv",'w',newline=''),["Key","Value"])
    trainernamescsv.writeheader()
    WriteData(trainernamescsv,trainernames)

    trainerFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\50.bin",'rb')
    trainer = ReadGenericData(trainerFile,TrainerName,False)
    trainercsv = csv.DictWriter(open("UKMR-TrainerData.csv",'w',newline=''),TrainerName)
    trainercsv.writeheader()
    WriteData(trainercsv,trainer)

    persStrFile = open(r"D:\UKMR\RomFS\string\UIString_EN-decomp\17.bin",'rb')
    persIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\17.bin",'rb')
    persnames = ReadENNames(persStrFile,persIntFile)
    persnamescsv = csv.DictWriter(open("UKMR-PersonalityNames.csv",'w',newline=''),["Key","Value"])
    persnamescsv.writeheader()
    WriteData(persnamescsv,persnames)

    persJPStrFile = open(r"D:\UKMR\RomFS\string\UIString_Jp\17.bin",'rb')
    persJPIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\17.bin",'rb')
    persJPnames = ReadJPNames(persJPStrFile,persJPIntFile)
    persJPnamescsv = csv.DictWriter(open("UKMR-PersonalityJPNames.csv",'w',encoding="utf-8",newline=''),["Key","Value"])
    persJPnamescsv.writeheader()
    WriteData(persJPnamescsv,persJPnames)

    personalityFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\8.bin",'rb')
    personality = ReadGenericData(personalityFile,PersonalityName,False)
    personalitycsv = csv.DictWriter(open("UKMR-PersonalityData.csv",'w',newline=''),PersonalityName)
    personalitycsv.writeheader()
    WriteData(personalitycsv,personality)

    monthlyItemFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\35.bin",'rb')
    monthlyItem = ReadGenericData(monthlyItemFile,MonthlyName,False)
    monthlyItemcsv = csv.DictWriter(open("UKMR-MonthlyItemData.csv",'w',newline=''),MonthlyName)
    monthlyItemcsv.writeheader()
    WriteData(monthlyItemcsv,monthlyItem)

    baseFoodFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\37.bin",'rb')
    baseFoods = ReadGenericData(baseFoodFile,BaseFoodName,False)
    baseFoodcsv = csv.DictWriter(open("UKMR-BaseFoodData.csv",'w',newline=''),BaseFoodName)
    baseFoodcsv.writeheader()
    WriteData(baseFoodcsv,baseFoods)

    spiceFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\38.bin",'rb')
    spices = ReadGenericData(spiceFile,SpiceName,False)
    spicecsv = csv.DictWriter(open("UKMR-SpiceData.csv",'w',newline=''),SpiceName)
    spicecsv.writeheader()
    WriteData(spicecsv,spices)

    mealStrFile = open(r"D:\UKMR\RomFS\string\UIString_EN-decomp\47.bin",'rb')
    mealIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\47.bin",'rb')
    mealnames = ReadENNames(mealStrFile,mealIntFile)
    mealnamescsv = csv.DictWriter(open("UKMR-MealNames.csv",'w',newline=''),["Key","Value"])
    mealnamescsv.writeheader()
    WriteData(mealnamescsv,mealnames)

    mealAttrStrFile = open(r"D:\UKMR\RomFS\string\UIString_EN-decomp\48.bin",'rb')
    mealAttrIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\48.bin",'rb')
    mealAttrnames = ReadENNames(mealAttrStrFile,mealAttrIntFile)
    mealAttrnamescsv = csv.DictWriter(open("UKMR-MealAttrNames.csv",'w',newline=''),["Key","Value"])
    mealAttrnamescsv.writeheader()
    WriteData(mealAttrnamescsv,mealAttrnames)

    mealFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\39.bin",'rb')
    meals = ReadGenericData(mealFile,MealName)
    mealcsv = csv.DictWriter(open("UKMR-MealData.csv",'w',newline=''),MealName)
    mealcsv.writeheader()
    WriteData(mealcsv,meals)

    effectRemap = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\43.bin",'rb')
    itemremap = ReadItemRemapData(effectRemap)
    itemFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\29.bin",'rb')
    items = ReadItemData(itemFile,itemremap)
    itemscsv = csv.DictWriter(open("UKMR-ItemData.csv",'w',newline=''),ItemName)
    itemscsv.writeheader()
    WriteData(itemscsv,items)

    consumableFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\34.bin",'rb')
    consumables = ReadGenericData(consumableFile,ConsumableName)
    consumablecsv = csv.DictWriter(open("UKMR-ConsumableData.csv",'w',newline=''),ConsumableName)
    consumablecsv.writeheader()
    WriteData(consumablecsv,consumables)

    itemNameStrFile = open(r"D:\UKMR\RomFS\string\UIString_EN-decomp\42.bin",'rb')
    itemNameIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\42.bin",'rb')
    itemnames = ReadENNames(itemNameStrFile,itemNameIntFile)
    itemnamescsv = csv.DictWriter(open("UKMR-ItemNames.csv",'w',newline=''),["Key","Value"])
    itemnamescsv.writeheader()
    WriteData(itemnamescsv,itemnames)

    techNameStrFile = open(r"D:\UKMR\RomFS\string\UIString_EN-decomp\23.bin",'rb')
    techNameIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\23.bin",'rb')
    technames = ReadENNames(techNameStrFile,techNameIntFile)
    technamescsv = csv.DictWriter(open("UKMR-TechNames.csv",'w',newline=''),["Key","Value"])
    technamescsv.writeheader()
    WriteData(technamescsv,technames)

    techJPStrFile = open(r"D:\UKMR\RomFS\string\UIString_Jp\23.bin",'rb')
    techJPIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\23.bin",'rb')
    techJPnames = ReadJPNames(techJPStrFile,techJPIntFile)
    techJPnamescsv = csv.DictWriter(open("UKMR-TechJPNames.csv",'w',encoding="utf-8",newline=''),["Key","Value"])
    techJPnamescsv.writeheader()
    WriteData(techJPnamescsv,techJPnames)

    techFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\12.bin",'rb')
    techs = ReadGenericData(techFile,TechName)
    techscsv = csv.DictWriter(open("UKMR-TechData.csv",'w',newline=''),TechName)
    techscsv.writeheader()
    WriteData(techscsv,techs)

    techLearnFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\13.bin",'rb')
    techlearn = ReadGenericData(techLearnFile,TechLearningName)
    techlearncsv = csv.DictWriter(open("UKMR-TechLearningData.csv",'w',newline=''),TechLearningName)
    techlearncsv.writeheader()
    WriteData(techlearncsv,techlearn)

    monsterNameStrFile = open(r"D:\UKMR\RomFS\string\UIString_EN-decomp\15.bin",'rb')
    monsterNameIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\15.bin",'rb')
    monsternames = ReadENNames(monsterNameStrFile,monsterNameIntFile)
    monsternamescsv = csv.DictWriter(open("UKMR-MonsterNames.csv",'w',newline=''),["Key","Value"])
    monsternamescsv.writeheader()
    WriteData(monsternamescsv,monsternames)

    monsterJPNameStrFile = open(r"D:\UKMR\RomFS\string\UIString_Jp\15.bin",'rb')
    monsterJPNameIntFile = open(r"D:\UKMR\RomFS\binary\UIStringExData-decomp\15.bin",'rb')
    monsterJPnames = ReadJPNames(monsterJPNameStrFile,monsterJPNameIntFile)
    monsterJPnamescsv = csv.DictWriter(open("UKMR-MonsterJPNames.csv",'w',encoding="utf-8",newline=''),["Key","Value"])
    monsterJPnamescsv.writeheader()
    WriteData(monsterJPnamescsv,monsterJPnames)

    breedData = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\3.bin",'rb')
    mainsub = ReadGenericData(breedData,MainSubName)
    mainsubcsv = csv.DictWriter(open("UKMR-MainSub.csv",'w',newline=''),MainSubName)
    mainsubcsv.writeheader()
    WriteData(mainsubcsv,mainsub)

    data = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\2.bin",'rb')
    monsters = ReadGenericData(data,DataName,False)
    csvFile = csv.DictWriter(open("UKMR-Monsters.csv",'w',newline=''),DataName)
    csvFile.writeheader()
    WriteData(csvFile,monsters)

MainFunction()