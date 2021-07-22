import struct
import sys
import os

def readUShort(file):
    return struct.unpack("H",file.read(2))[0]

def readUInt(file):
    return struct.unpack("I",file.read(4))[0]

class TXPFile:
    def __init__(self,name,offset):
        self.name = name
        self.offset = offset
        self.length = 0

def ExportTXPs(inFile):
    fileCount = readUShort(inFile)
    fileInfo = []
    for _ in range(fileCount):
        nameSize = int(inFile.read(1)[0])
        name = inFile.read(nameSize)
        offset = readUInt(inFile)
        fileInfo.append(TXPFile(name.decode('utf-8'),offset))
    #generate lengths
    for i in range(len(fileInfo)):
        if i == len(fileInfo)-1:
            fileInfo[i].length = os.stat(inFile.name).st_size - fileInfo[i].offset
        else:
            fileInfo[i].length = fileInfo[i+1].offset - fileInfo[i].offset
    for file in fileInfo:
        #now we have all of the info needed
        basePath = inFile.name.split('.')[0]+'/'
        os.makedirs(basePath,exist_ok=True)
        nFile = open(basePath+file.name+".txp",'wb')
        inFile.seek(file.offset)
        nFile.write(inFile.read(file.length))
        nFile.close()
    


if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if i > 0:
            ExportTXPs(open(arg,'rb'))