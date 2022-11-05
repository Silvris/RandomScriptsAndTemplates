import os
from pathlib import Path
import sys
import zlib
import struct

def readUInt(file):
    return struct.unpack("I",file.read(4))[0]

def align(file, modulo, offset):
    current = file.tell() - offset
    over = current % modulo
    if(over != 0):
        remaining = modulo - over
        file.seek(file.tell()+remaining)

def readGz(f,index):
    offset = f.tell()
    print(offset)
    basePath = f.name
    #os.makedirs(basePath,exist_ok=True)
    flags = readUInt(f) #currently unknown if these are important
    fileNum = readUInt(f) #number of files present within the container
    decompTotal = readUInt(f) #useless for us, appears to be a total size of all decompressed files, maybe used for generating an output byte array by the engine
    compSizes = list()
    for _ in range(fileNum):
        compSizes.append(readUInt(f)) #note, we won't actually be using these
        #each file gives a more accurate size at its start
    align(f,128,offset)
    output = bytearray()
    for i in range(fileNum):
        #time for the magic
        fileSize = readUInt(f)
        compData = f.read(fileSize)
        #go ahead and realign for the next file
        align(f,128,offset)
        #now decompress
        print(len(compData))
        decompData = zlib.decompress(compData)
        output.extend(decompData)
    path = basePath.replace(".bin","")
    os.makedirs(path,exist_ok=True)
    nFile = open(path+"/{}.bin".format(index),'wb')
    nFile.write(output)
    nFile.close()

def readFile(f):
    assert readUInt(f) == 1179407431
    readUInt(f)
    num = readUInt(f)
    unkn = readUInt(f)
    fileInfo = list()
    for i in range(num):
        fileInfo.append([readUInt(f),readUInt(f),readUInt(f)])
    for i in range(num):
        f.seek(fileInfo[i][0])
        readGz(f,i)

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if i > 0:
            readFile(open(arg,'rb'))