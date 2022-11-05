from re import T
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

for i in range(4,22):
    TechName["Unkn{}".format(i)] = True

for i in range(5,15):
    MonthlyName["Unkn{}".format(i)] = True

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

    trainerStrFile = open(r"I:\UKMR\RomFS\string\UIString_EN-decomp\51.bin",'rb')
    trainerIntFile = open(r"I:\UKMR\RomFS\binary\UIStringExData-decomp\51.bin",'rb')
    trainernames = ReadENNames(trainerStrFile,trainerIntFile)
    trainernamescsv = csv.DictWriter(open("UKMR-TrainerNames.csv",'w',newline=''),["Key","Value"])
    trainernamescsv.writeheader()
    WriteData(trainernamescsv,trainernames)

    trainerFile = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\50.bin",'rb')
    trainer = ReadGenericData(trainerFile,TrainerName,False)
    trainercsv = csv.DictWriter(open("UKMR-TrainerData.csv",'w',newline=''),TrainerName)
    trainercsv.writeheader()
    WriteData(trainercsv,trainer)

    persStrFile = open(r"I:\UKMR\RomFS\string\UIString_EN-decomp\17.bin",'rb')
    persIntFile = open(r"I:\UKMR\RomFS\binary\UIStringExData-decomp\17.bin",'rb')
    persnames = ReadENNames(persStrFile,persIntFile)
    persnamescsv = csv.DictWriter(open("UKMR-PersonalityNames.csv",'w',newline=''),["Key","Value"])
    persnamescsv.writeheader()
    WriteData(persnamescsv,persnames)

    persJPStrFile = open(r"I:\UKMR\RomFS\string\UIString_Jp\17.bin",'rb')
    persJPIntFile = open(r"I:\UKMR\RomFS\binary\UIStringExData-decomp\17.bin",'rb')
    persJPnames = ReadJPNames(persJPStrFile,persJPIntFile)
    persJPnamescsv = csv.DictWriter(open("UKMR-PersonalityJPNames.csv",'w',encoding="utf-8",newline=''),["Key","Value"])
    persJPnamescsv.writeheader()
    WriteData(persJPnamescsv,persJPnames)

    personalityFile = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\8.bin",'rb')
    personality = ReadGenericData(personalityFile,PersonalityName,False)
    personalitycsv = csv.DictWriter(open("UKMR-PersonalityData.csv",'w',newline=''),PersonalityName)
    personalitycsv.writeheader()
    WriteData(personalitycsv,personality)

    monthlyItemFile = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\35.bin",'rb')
    monthlyItem = ReadGenericData(monthlyItemFile,MonthlyName,False)
    monthlyItemcsv = csv.DictWriter(open("UKMR-MonthlyItemData.csv",'w',newline=''),MonthlyName)
    monthlyItemcsv.writeheader()
    WriteData(monthlyItemcsv,monthlyItem)

    baseFoodFile = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\37.bin",'rb')
    baseFoods = ReadGenericData(baseFoodFile,BaseFoodName,False)
    baseFoodcsv = csv.DictWriter(open("UKMR-BaseFoodData.csv",'w',newline=''),BaseFoodName)
    baseFoodcsv.writeheader()
    WriteData(baseFoodcsv,baseFoods)

    spiceFile = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\38.bin",'rb')
    spices = ReadGenericData(spiceFile,SpiceName,False)
    spicecsv = csv.DictWriter(open("UKMR-SpiceData.csv",'w',newline=''),SpiceName)
    spicecsv.writeheader()
    WriteData(spicecsv,spices)

    mealStrFile = open(r"I:\UKMR\RomFS\string\UIString_EN-decomp\47.bin",'rb')
    mealIntFile = open(r"I:\UKMR\RomFS\binary\UIStringExData-decomp\47.bin",'rb')
    mealnames = ReadENNames(mealStrFile,mealIntFile)
    mealnamescsv = csv.DictWriter(open("UKMR-MealNames.csv",'w',newline=''),["Key","Value"])
    mealnamescsv.writeheader()
    WriteData(mealnamescsv,mealnames)

    mealAttrStrFile = open(r"I:\UKMR\RomFS\string\UIString_EN-decomp\48.bin",'rb')
    mealAttrIntFile = open(r"I:\UKMR\RomFS\binary\UIStringExData-decomp\48.bin",'rb')
    mealAttrnames = ReadENNames(mealAttrStrFile,mealAttrIntFile)
    mealAttrnamescsv = csv.DictWriter(open("UKMR-MealAttrNames.csv",'w',newline=''),["Key","Value"])
    mealAttrnamescsv.writeheader()
    WriteData(mealAttrnamescsv,mealAttrnames)

    mealFile = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\39.bin",'rb')
    meals = ReadGenericData(mealFile,MealName)
    mealcsv = csv.DictWriter(open("UKMR-MealData.csv",'w',newline=''),MealName)
    mealcsv.writeheader()
    WriteData(mealcsv,meals)

    effectRemap = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\43.bin",'rb')
    itemremap = ReadItemRemapData(effectRemap)
    itemFile = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\29.bin",'rb')
    items = ReadItemData(itemFile,itemremap)
    itemscsv = csv.DictWriter(open("UKMR-ItemData.csv",'w',newline=''),ItemName)
    itemscsv.writeheader()
    WriteData(itemscsv,items)

    consumableFile = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\34.bin",'rb')
    consumables = ReadGenericData(consumableFile,ConsumableName)
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

    techJPStrFile = open(r"I:\UKMR\RomFS\string\UIString_Jp\23.bin",'rb')
    techJPIntFile = open(r"I:\UKMR\RomFS\binary\UIStringExData-decomp\23.bin",'rb')
    techJPnames = ReadJPNames(techJPStrFile,techJPIntFile)
    techJPnamescsv = csv.DictWriter(open("UKMR-TechJPNames.csv",'w',encoding="utf-8",newline=''),["Key","Value"])
    techJPnamescsv.writeheader()
    WriteData(techJPnamescsv,techJPnames)

    techFile = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\12.bin",'rb')
    techs = ReadGenericData(techFile,TechName)
    techscsv = csv.DictWriter(open("UKMR-TechData.csv",'w',newline=''),TechName)
    techscsv.writeheader()
    WriteData(techscsv,techs)

    techLearnFile = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\13.bin",'rb')
    techlearn = ReadGenericData(techLearnFile,TechLearningName)
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
    mainsub = ReadGenericData(breedData,MainSubName)
    mainsubcsv = csv.DictWriter(open("UKMR-MainSub.csv",'w',newline=''),MainSubName)
    mainsubcsv.writeheader()
    WriteData(mainsubcsv,mainsub)

    data = open(r"I:\UKMR\RomFS\binary\ConstData_US-decomp\2.bin",'rb')
    monsters = ReadGenericData(data,DataName)
    csvFile = csv.DictWriter(open("UKMR-Monsters.csv",'w',newline=''),DataName)
    csvFile.writeheader()
    WriteData(csvFile,monsters)

MainFunction()