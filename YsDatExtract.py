import struct
import os
from pathlib import Path

pakPath = r"C:\Users\Owner\Downloads\Programs\Ys\DAT.PAK"
pkiPath = r"C:\Users\Owner\Downloads\Programs\Ys\DAT.PKI"
outputPath = r"C:\Users\Owner\Downloads\Programs\Ys\\"

def readUInt(file):
    return struct.unpack("I",file.read(4))[0]

def removeNulls(array):
    arr = bytearray()
    for i in range(len(array)):
        if array[i] != 0x00:
            arr.append(array[i])
    return bytes(arr)

def extractPAK():
    os.chdir(outputPath)
    pak = open(pakPath,'rb')
    pki = open(pkiPath,'rb')
    pkiMagic = readUInt(pki)
    #print(pkiMagic)
    if pkiMagic != 0x6678:
        print("Invalid magic bytes!")
        return
    fileCount = readUInt(pki)
    pki.read(8)
    for _ in range(fileCount):
        nameArray = pki.read(256)
        nameArray = removeNulls(nameArray)
        name = nameArray.decode("utf-8")
        offset = readUInt(pki)
        size = readUInt(pki)
        pak.seek(offset)
        newFile = pak.read(size)
        dirPath = os.path.split(name)[0]
        #print(dirPath, 1)
        if(dirPath != ''):
            os.makedirs(dirPath,exist_ok=True)
        outFile = open(name,'wb')
        outFile.write(newFile)
        outFile.close()

def extractPKMs():
    for path in Path(outputPath).rglob("*.pkm"):
        names = []
        offsets = []
        sizes = []
        pkm = open(path,'rb')
        pkmMagic = readUInt(pkm)
        #print(pkmMagic)
        if pkmMagic != 0x6678:
            print("Invalid magic bytes!")
            return
        fileCount = readUInt(pkm)
        pkm.read(8)
        for _ in range(fileCount):
            nameArray = pkm.read(256)
            nameArray = removeNulls(nameArray)
            name = nameArray.decode("utf-8")
            offset = readUInt(pkm)
            size = readUInt(pkm)
            names.append(name)
            offsets.append(offset)
            sizes.append(size)
        while(pkm.tell()%64 !=0):
            pkm.read(1)
        startOff = pkm.tell()
        for i in range(fileCount):
            pkm.seek(startOff+offsets[i])
            newFile = pkm.read(sizes[i])
            dirPath = os.path.split(names[i])[0]
            print(names[i])
            if(dirPath != ''):
                os.makedirs(dirPath,exist_ok=True)
            outFile = open(names[i],'wb')
            outFile.write(newFile)
            outFile.close()

extractPAK()
extractPKMs()