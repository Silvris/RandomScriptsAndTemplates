import zlib
import lzss
import struct
import os
from pathlib import Path

def decompressMaps():
    for path in Path(r"D:\Games\[C77] [Daissessen] LETHAL・CRISIS\map").rglob("*"):
        newPath = str(path).replace("map","decompMap")
        file = open(path,'rb')
        file.seek(8)
        data = file.read()
        decompData = zlib.decompress(data)
        newFile = open(newPath,'wb')
        newFile.write(decompData)
        newFile.close()
        file.close()


def decompressLZSS(file,fileName):
    magic = file[0:4]
    #print(magic)
    if (magic == b'LZSS'):
        compFile = file[8:]
        #decompFile = file
        decompFile = lzss.decompress(compFile)
        dirPath = os.path.split(fileName)[0]
        #print(dirPath, 1)
        if(dirPath != ''):
            os.makedirs(dirPath,exist_ok=True)
        outFile = open(fileName,'wb')
        outFile.write(decompFile)
    else:
        #file is uncompressed
        outFile = open(fileName,'wb')
        outFile.write(file)

def removeNulls(array):
    arr = bytearray()
    for i in range(len(array)):
        if array[i] != 0x00:
            arr.append(array[i])
    return bytes(arr)
    

def readPACK(file):
    magic = file.read(4)
    assert magic == b'PACK'
    fileCount = struct.unpack("I",file.read(4))[0]
    for _ in range(fileCount):
        nameArray = file.read(64)
        nameArray = removeNulls(nameArray)
        name = nameArray.decode('shift-jis')
        unkn1 = file.read(4)
        unkn2 = file.read(4)
        offset = struct.unpack("I",file.read(4))[0]
        size = struct.unpack("I",file.read(4))[0]
        current = file.tell()
        file.seek(offset)
        outFile = file.read(size)
        decompressLZSS(outFile,name)
        file.seek(current)

os.chdir(r"D:\Games\[C77] [Daissessen] LETHAL・CRISIS")
packPath = r"リーサルクライシス.p"

readPACK(open(packPath,'rb'))
#decompressMaps()