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

for i in range(4,22):
    TechName["Unkn{}".format(i)] = True

for i in range(5,15):
    MonthlyName["Unkn{}".format(i)] = True

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

    fusionItemFile = open(r"D:\UKMR\JPRomFS\binary\ConstData\36.bin",'rb')
    fusionItem = ReadGenericData(fusionItemFile,FusionItemName,False)
    fusionItemcsv = csv.DictWriter(open("UKMR-FusionItemDataJP.csv",'w',newline=''),FusionItemName)
    fusionItemcsv.writeheader()
    WriteData(fusionItemcsv,fusionItem)

    mbFile = open(r"D:\UKMR\JPRomFS\binary\ConstData\4.bin",'rb')
    mainbreed = ReadGenericData(mbFile,MainBreedName,False)
    mainbreedcsv = csv.DictWriter(open("UKMR-MainBreedDataJP.csv",'w',newline=''),MainBreedName)
    mainbreedcsv.writeheader()
    WriteData(mainbreedcsv,mainbreed)

    trainerFile = open(r"D:\UKMR\JPRomFS\binary\ConstData\50.bin",'rb')
    trainer = ReadGenericData(trainerFile,TrainerName,False)
    trainercsv = csv.DictWriter(open("UKMR-TrainerDataJP.csv",'w',newline=''),TrainerName)
    trainercsv.writeheader()
    WriteData(trainercsv,trainer)

    personalityFile = open(r"D:\UKMR\JPRomFS\binary\ConstData\8.bin",'rb')
    personality = ReadGenericData(personalityFile,PersonalityName,False)
    personalitycsv = csv.DictWriter(open("UKMR-PersonalityDataJP.csv",'w',newline=''),PersonalityName)
    personalitycsv.writeheader()
    WriteData(personalitycsv,personality)

    monthlyItemFile = open(r"D:\UKMR\JPRomFS\binary\ConstData\35.bin",'rb')
    monthlyItem = ReadGenericData(monthlyItemFile,MonthlyName,False)
    monthlyItemcsv = csv.DictWriter(open("UKMR-MonthlyItemDataJP.csv",'w',newline=''),MonthlyName)
    monthlyItemcsv.writeheader()
    WriteData(monthlyItemcsv,monthlyItem)

    baseFoodFile = open(r"D:\UKMR\JPRomFS\binary\ConstData\37.bin",'rb')
    baseFoods = ReadGenericData(baseFoodFile,BaseFoodName,False)
    baseFoodcsv = csv.DictWriter(open("UKMR-BaseFoodDataJP.csv",'w',newline=''),BaseFoodName)
    baseFoodcsv.writeheader()
    WriteData(baseFoodcsv,baseFoods)

    spiceFile = open(r"D:\UKMR\JPRomFS\binary\ConstData\38.bin",'rb')
    spices = ReadGenericData(spiceFile,SpiceName,False)
    spicecsv = csv.DictWriter(open("UKMR-SpiceDataJP.csv",'w',newline=''),SpiceName)
    spicecsv.writeheader()
    WriteData(spicecsv,spices)

    mealFile = open(r"D:\UKMR\JPRomFS\binary\ConstData\39.bin",'rb')
    meals = ReadGenericData(mealFile,MealName)
    mealcsv = csv.DictWriter(open("UKMR-MealDataJP.csv",'w',newline=''),MealName)
    mealcsv.writeheader()
    WriteData(mealcsv,meals)

    effectRemap = open(r"D:\UKMR\JPRomFS\binary\ConstData\43.bin",'rb')
    itemremap = ReadItemRemapData(effectRemap)
    itemFile = open(r"D:\UKMR\JPRomFS\binary\ConstData\29.bin",'rb')
    items = ReadItemData(itemFile,itemremap)
    itemscsv = csv.DictWriter(open("UKMR-ItemDataJP.csv",'w',newline=''),ItemName)
    itemscsv.writeheader()
    WriteData(itemscsv,items)

    consumableFile = open(r"D:\UKMR\JPRomFS\binary\ConstData\34.bin",'rb')
    consumables = ReadGenericData(consumableFile,ConsumableName)
    consumablecsv = csv.DictWriter(open("UKMR-ConsumableDataJP.csv",'w',newline=''),ConsumableName)
    consumablecsv.writeheader()
    WriteData(consumablecsv,consumables)

    techFile = open(r"D:\UKMR\JPRomFS\binary\ConstData\12.bin",'rb')
    techs = ReadGenericData(techFile,TechName)
    techscsv = csv.DictWriter(open("UKMR-TechDataJP.csv",'w',newline=''),TechName)
    techscsv.writeheader()
    WriteData(techscsv,techs)

    techLearnFile = open(r"D:\UKMR\JPRomFS\binary\ConstData\13.bin",'rb')
    techlearn = ReadGenericData(techLearnFile,TechLearningName)
    techlearncsv = csv.DictWriter(open("UKMR-TechLearningDataJP.csv",'w',newline=''),TechLearningName)
    techlearncsv.writeheader()
    WriteData(techlearncsv,techlearn)

    breedData = open(r"D:\UKMR\JPRomFS\binary\ConstData\3.bin",'rb')
    mainsub = ReadGenericData(breedData,MainSubName)
    mainsubcsv = csv.DictWriter(open("UKMR-MainSubJP.csv",'w',newline=''),MainSubName)
    mainsubcsv.writeheader()
    WriteData(mainsubcsv,mainsub)

    data = open(r"D:\UKMR\JPRomFS\binary\ConstData\2.bin",'rb')
    monsters = ReadGenericData(data,DataName,False)
    csvFile = csv.DictWriter(open("UKMR-MonstersJP.csv",'w',newline=''),DataName)
    csvFile.writeheader()
    WriteData(csvFile,monsters)

MainFunction()