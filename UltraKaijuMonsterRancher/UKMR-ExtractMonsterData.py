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

DataName = [
    "Index",
    "Variation",
    "BaseLif",
    "BasePow",
    "BaseInt",
    "BaseSki",
    "BaseSpd",
    "BaseDef",
    "LifGain",
    "PowGain",
    "IntGain",
    "SkiGain",
    "SpdGain",
    "DefGain",
    "ForwardMov",
    "BackwardsMov",
    "GutsRcvr",
    "Lifespan"
]
for i in range(3,22):
    DataName.append("Unkn{}".format(i))

MainSubName  = [
    "Index",
    "Name",
    "Unkn1",
    "Unkn2",
    "LifeType"
]

for i in range(3,22):
    MainSubName.append("Unkn{}".format(i))

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

TechLearningName = [
    "Index",
    "MainBreed",
    "SpecificMainSub",
    "ExcludeMainSub",
    "Unkn1",
    "TechIndex",
    "Unkn2",
    "Unkn3",
    "RequiredStat",
    "RequiredNumerical",
    "Unkn4",
    "Unkn5"
]

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

ConsumableName = [
    "Index",
    "Unkn1",
    "Unkn2",
    "Unkn3",
    "Unkn4",
    "Unkn5",
    "Unkn6",
    "Unkn7",
    "Unkn8",
    "Unkn9",
    "Unkn10",
    "Unkn11",
    "Unkn12",
    "Unkn13",
    "Unkn14",
    "Unkn15",
    "Lifespan",
    "Unkn16", #percent lifespan?
    "Dependency",
    "PercentDependency",
    "Fear",
    "PercentFear",
    "Unkn19",
    "Unkn20",
    "Fatigue",
    "PercentFatigue",
    "Stress",
    "PercentStress", #Stress
    "Weight",
    "PercentWeight",
    "Anger",
    "PercentAnger",
    "Life",
    "Power",
    "Intelligence",
    "Skill",
    "Speed",
    "Defense",
    "Unkn26"
]

for i in range(4,22):
    TechName["Unkn{}".format(i)] = True

def GenerateRemap():
    p2 = csv.DictReader(open("NameRemapP2.csv",'r',newline=''))
    part2 = dict()
    for row in p2:
        part2[row["Name"]] = row["Index"]
    return part2

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

def ReadConsumableData(f):
    items = list()
    itemNum = readInt(f)
    for i in range(itemNum):
        item = dict()
        for field in ConsumableName:
                datatype = f.read(1)
                #branch on known datatypes
                #print(datatype)
                if datatype == b"\x00":
                    item[field] = readInt(f)
                elif datatype == b"\x01":
                    item[field] = round(readFloat(f),1)
                else:
                    return items
        items.append(item)
    return items

def ReadTechLearningData(f):
    techs = list()
    techNum = readInt(f)
    for i in range(techNum):
        tech = dict()
        tech["Index"] = i
        for field in TechLearningName:
            if field != "Index":
                datatype = f.read(1)
                #branch on known datatypes
                #print(datatype)
                if datatype == b"\x00":
                    tech[field] = readInt(f)
                elif datatype == b"\x01":
                    tech[field] = round(readFloat(f),1)
                else:
                    return techs
        techs.append(tech)
    return techs

def ReadTechData(f):
    techs = list()
    techNum = readInt(f)
    for i in range(techNum):
        tech = dict()
        tech["Index"] = i
        for field in TechName:
            if field != "Index":
                datatype = f.read(1)
                #branch on known datatypes
                #print(datatype)
                if datatype == b"\x00":
                    if TechName[field] == True:
                        tech[field] = readInt(f)
                    else:
                        tech[field] = readUInt(f)
                elif datatype == b"\x01":
                    tech[field] = round(readFloat(f),1)
                else:
                    return techs
        techs.append(tech)
    return techs

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
            "Value":strings[i]
        })
    return names


def ReadMonsterBreedData(f):
    monsters = list()
    monsterDataNum = readInt(f)
    for i in range(monsterDataNum):
        monster = dict()
        monster["Index"] = i
        for field in MainSubName:
            if field != "Index":
                datatype = f.read(1)
                #branch on known datatypes
                #print(datatype)
                if datatype == b"\x00":
                    monster[field] = readUInt(f)
                    if monster[field] == 0xFFFFFFFF:
                        monster[field] = -1
                elif datatype == b"\x01":
                    monster[field] = round(readFloat(f),1)
                else:
                    return monsters
        #now remap index
        #print(monster["Name"])
        monsters.append(monster)
    return monsters


def ReadMonsterData(f):
    monsters = list()
    monsterDataNum = readInt(f)
    for i in range(monsterDataNum):
        monster = dict()
        for field in DataName:
            datatype = f.read(1)
            #branch on known datatypes
            #print(datatype)
            if datatype == b"\x00":
                monster[field] = readInt(f)
            elif datatype == b"\x01":
                monster[field] = round(readFloat(f),1)
            else:
                return monsters
        monsters.append(monster)
    return monsters

def WriteData(f, monsters):
    for monster in monsters:
        f.writerow(monster)


def MainFunction():
    #remap = GenerateRemap()
    #print(remap)

    effectRemap = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\43.bin",'rb')
    itemremap = ReadItemRemapData(effectRemap)
    itemFile = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\29.bin",'rb')
    items = ReadItemData(itemFile,itemremap)
    itemscsv = csv.DictWriter(open("UKMR-ItemData.csv",'w',newline=''),ItemName)
    itemscsv.writeheader()
    WriteData(itemscsv,items)

    consumableFile = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\34.bin",'rb')
    consumables = ReadConsumableData(consumableFile)
    consumablecsv = csv.DictWriter(open("UKMR-ConsumableData.csv",'w',newline=''),ConsumableName)
    consumablecsv.writeheader()
    WriteData(consumablecsv,consumables)

    itemNameStrFile = open(r"I:\UKMR\RomFS\string\UIString_EN-decomp\42.bin",'rb')
    itemNameIntFile = open(r"I:\UKMR\RomFS\binary\UIStringExData-decomp\42.bin",'rb')
    itemnames = ReadENNames(itemNameStrFile,itemNameIntFile)
    itemnamescsv = csv.DictWriter(open("UKMR-ItemNames.csv",'w',newline=''),["Key","Value"])
    itemnamescsv.writeheader()
    WriteData(itemnamescsv,itemnames)

    techNameStrFile = open(r"I:\UKMR\RomFS\string\UIString_EN-decomp\23.bin",'rb')
    techNameIntFile = open(r"I:\UKMR\RomFS\binary\UIStringExData-decomp\23.bin",'rb')
    technames = ReadENNames(techNameStrFile,techNameIntFile)
    technamescsv = csv.DictWriter(open("UKMR-TechNames.csv",'w',newline=''),["Key","Value"])
    technamescsv.writeheader()
    WriteData(technamescsv,technames)

    techFile = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\12.bin",'rb')
    techs = ReadTechData(techFile)
    techscsv = csv.DictWriter(open("UKMR-TechData.csv",'w',newline=''),TechName)
    techscsv.writeheader()
    WriteData(techscsv,techs)

    techLearnFile = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\13.bin",'rb')
    techlearn = ReadTechLearningData(techLearnFile)
    techlearncsv = csv.DictWriter(open("UKMR-TechLearningData.csv",'w',newline=''),TechLearningName)
    techlearncsv.writeheader()
    WriteData(techlearncsv,techlearn)

    monsterNameStrFile = open(r"I:\UKMR\RomFS\string\UIString_EN-decomp\15.bin",'rb')
    monsterNameIntFile = open(r"I:\UKMR\RomFS\binary\UIStringExData-decomp\15.bin",'rb')
    monsternames = ReadENNames(monsterNameStrFile,monsterNameIntFile)
    monsternamescsv = csv.DictWriter(open("UKMR-MonsterNames.csv",'w',newline=''),["Key","Value"])
    monsternamescsv.writeheader()
    WriteData(monsternamescsv,monsternames)

    monsterJPNameStrFile = open(r"I:\UKMR\RomFS\string\UIString_Jp\15.bin",'rb')
    monsterJPNameIntFile = open(r"I:\UKMR\RomFS\binary\UIStringExData-decomp\15.bin",'rb')
    monsterJPnames = ReadJPNames(monsterJPNameStrFile,monsterJPNameIntFile)
    monsterJPnamescsv = csv.DictWriter(open("UKMR-MonsterJPNames.csv",'w',encoding="utf-8",newline=''),["Key","Value"])
    monsterJPnamescsv.writeheader()
    WriteData(monsterJPnamescsv,monsterJPnames)

    breedData = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\3.bin",'rb')
    mainsub = ReadMonsterBreedData(breedData)
    mainsubcsv = csv.DictWriter(open("UKMR-MainSub.csv",'w',newline=''),MainSubName)
    mainsubcsv.writeheader()
    WriteData(mainsubcsv,mainsub)

    data = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\2.bin",'rb')
    monsters = ReadMonsterData(data)
    csvFile = csv.DictWriter(open("UKMR-Monsters.csv",'w',newline=''),DataName)
    csvFile.writeheader()
    WriteData(csvFile,monsters)

MainFunction()