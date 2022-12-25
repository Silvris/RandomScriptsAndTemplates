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

BalanceNames ={
    "Price":True,
    "Monster1":True,
    "Monster2":True
}

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
        if monster["Monster1"] != -1 or monster["Monster2"] != -1:
            f.writerow(monster)


def MainFunction():

    balanceFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\65.bin",'rb')
    balance = ReadGenericData(balanceFile,BalanceNames,False)
    balancecsv = csv.DictWriter(open("UKMR-BalanceData.csv",'w',newline=''),BalanceNames)
    balancecsv.writeheader()
    WriteData(balancecsv,balance)

    balanceFile = open(r"D:\UKMR\RomFS\binary\ConstData_US-decomp\66.bin",'rb')
    balance = ReadGenericData(balanceFile,BalanceNames,False)
    balancecsv = csv.DictWriter(open("UKMR-Balance2Data.csv",'w',newline=''),BalanceNames)
    balancecsv.writeheader()
    WriteData(balancecsv,balance)

MainFunction()