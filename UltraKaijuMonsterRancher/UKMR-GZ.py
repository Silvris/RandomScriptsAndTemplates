import os
from pathlib import Path
import sys
import zlib
import struct

def readUInt(file):
    return struct.unpack("I",file.read(4))[0]

def align(file, modulo):
    current = file.tell()
    over = current % modulo
    if(over != 0):
        remaining = modulo - over
        file.seek(current+remaining)

def readFile(f):
    basePath = f.name
    #os.makedirs(basePath,exist_ok=True)
    flags = readUInt(f) #currently unknown if these are important
    fileNum = readUInt(f) #number of files present within the container
    decompTotal = readUInt(f) #useless for us, appears to be a total size of all decompressed files, maybe used for generating an output byte array by the engine
    compSizes = list()
    for _ in range(fileNum):
        compSizes.append(readUInt(f)) #note, we won't actually be using these
        #each file gives a more accurate size at its start
    align(f,128)
    output = bytearray()
    for i in range(fileNum):
        #time for the magic
        fileSize = readUInt(f)
        compData = f.read(fileSize)
        #go ahead and realign for the next file
        align(f,128)
        #now decompress
        decompData = zlib.decompress(compData)
        output.extend(decompData)
    nFile = open(basePath.replace(".gz",""),'wb')
    nFile.write(output)
    nFile.close()

if __name__ == "__main__":
    for path in Path(r"I:UKMR").rglob("*.gz"):
        print(path)
        if os.path.getsize(path) > 0:
            try:
                readFile(open(path,'rb'))
            except:
                print("Failed:{}".format(path))