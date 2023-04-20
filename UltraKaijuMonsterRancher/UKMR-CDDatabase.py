from io import SEEK_END, SEEK_SET
import struct
import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

CDData = dict()

def readInt(file):
    #print(file.tell())
    return struct.unpack("i",file.read(4))[0]

def readUInt(file):
    #print(file.tell())
    return struct.unpack("I",file.read(4))[0]

def readUShort(file):
    #print(file.tell())
    return struct.unpack("H",file.read(2))[0]

def ReadMonsterMap(file):
    file.seek(0, SEEK_END)
    filesize = file.tell()
    file.seek(0, SEEK_SET)
    while file.tell() < filesize:
        idx = readUInt(file)
        if CDData[idx] == None:
            CDData[idx] = dict()
        CDData[idx]["Unkn2"] = readUInt(file)
        CDData[idx]["Monster"] = readUShort(file)
        CDData[idx]["Unkn3"] = readUShort(file)
    
def ParseCDTSV(tsv):
    assert isinstance(tsv, csv.DictReader)
    for row in tsv:
        idx = int(row["Index"])
        if idx not in CDData:
            CDData[idx] = dict()
        CDData[idx]["Index"] = idx
        CDData[idx]["Name"] = row["Name"].replace("\r","").replace("\n","")
        CDData[idx]["Artist"] = row["Artist"].replace("\r","").replace("\n","")
        CDData[idx]["Unkn1"] = row["Unk"].replace("\r","").replace("\n","")


def WriteData(f, data):
    for row in data:
        f.writerow(data[row])


def MainFunction():
    ParseCDTSV(csv.DictReader(open(r"D:\UKMR\JPRomFS\binary\CDDataBase_JP\2 - Copy.txt",'r',encoding='utf-8'),["Name","Artist","Index","Unk"],delimiter="\t"))
    ReadMonsterMap(open(r"D:\UKMR\JPRomFS\binary\CDDataBase_JP\4.bin",'rb'))
    dbfile = open("UKMR-JPCDDatabase.csv",'w', encoding='utf-8',newline='')
    db = csv.DictWriter(dbfile,["Index","Name","Artist","Monster","Unkn1","Unkn2","Unkn3"])
    db.writeheader()
    WriteData(db,CDData)

MainFunction()