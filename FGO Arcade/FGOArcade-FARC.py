import gzip
import struct
import os
import zstd
import sys

def readUInt(file):
    return struct.unpack(">I",file.read(4))[0]

def readLEUInt(file):
    return struct.unpack("I",file.read(4))[0]

def readNullTerminatedString(file):
    currentByte = file.read(1)
    string = bytearray()
    while(1):
        if currentByte == b'':
            return ""
            #this is python's method of EOF
        elif currentByte == b'\x00':
            return string.decode('utf-8')
        else:
            string.extend(currentByte)
        currentByte = file.read(1)

class Entry:
    def __init__(self,name,offset,compSize,uncompSize,flags):
        self.name = name
        self.offset = offset
        self.compSize = compSize
        self.uncompSize = uncompSize
        self.flags = flags

FARCHeads = [b'FARc',b'FARC']

def ReadFARC(inFile):
    entries = []
    assert inFile.read(4) in FARCHeads
    inFile.read(4)#header length
    inFile.read(4)#file flags, doesn't seem to matter too much
    inFile.read(4)
    inFile.read(4)#alignment
    Format = readUInt(inFile)
    entryCount = readUInt(inFile)
    inFile.read(4)
    for _ in range(entryCount):
        eName = readNullTerminatedString(inFile)
        eOff = readUInt(inFile)
        eComp = readUInt(inFile)
        eUncomp = readUInt(inFile)
        eFlags = readUInt(inFile)
        entries.append(Entry(eName,eOff,eComp,eUncomp,eFlags))
    
    for entry in entries:
        basePath = inFile.name.split('.')[0]+'/'
        os.makedirs(basePath,exist_ok=True)
        nFile = open(basePath+entry.name,'wb')
        #read filedata from archive
        inFile.seek(entry.offset)
        #now check flags
        subFiles = []
        if entry.flags != 0:
            #first check for sub-files
            if entry.flags & 16 != 0:
                #sub-files present
                inFile.read(4)#small header, doesn't seem to affect anything
                lengths = []
                length = readLEUInt(inFile)
                while length != 4247762216 and length != 134777631: #zstd and gzip respectively
                    lengths.append(length)
                    length = readLEUInt(inFile)
                inFile.seek(inFile.tell()-4)
                for i in range(len(lengths)):
                    
                    subFiles.append(inFile.read(lengths[i]))
            else:
                subFiles.append(inFile.read(entry.compSize))
            #check for compression
            if entry.flags & 2 != 0:
                #gzip compression
                for i in range(len(subFiles)):
                    print(subFiles[i][0:4])
                    subFiles[i] = gzip.decompress(subFiles[i])
            elif entry.flags & 32 != 0:
                #zstd compression
                for i in range(len(subFiles)):
                    subFiles[i] = zstd.decompress(subFiles[i])
            #reassemble the file
            fileData = bytearray()
            for i in range(len(subFiles)):
                fileData.extend(subFiles[i])
        else:
            fileData = inFile.read(entry.compSize)
        nFile.write(fileData)
        nFile.close()

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if i > 0:
            ReadFARC(open(arg,'rb'))
