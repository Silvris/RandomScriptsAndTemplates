from io import BufferedReader, BufferedWriter
import sys
import os
import struct


def readUInt(file):
    return struct.unpack("I",file.read(4))[0]


def writeUInt(file,val):
    file.write(struct.pack("I",val))

def ReadWavIntoDict(file,outDict):
    assert isinstance(file,BufferedReader)
    assert isinstance(outDict,dict)
    assert file.read(4) == b"RIFF"
    fileSize = readUInt(file) + 8 #filesize following RIFF header of 8 bytes
    assert file.read(4) == b"WAVE"
    #now to section processing
    while file.tell() < fileSize:
        magic = file.read(4)
        size = readUInt(file)
        data = file.read(size)
        outDict[magic] = data

def WriteWavFromDict(file,inDict):
    assert isinstance(file,BufferedWriter)
    assert isinstance(inDict,dict)
    file.write(b"RIFF")
    #now calculate filelength
    fileLength = 4
    for key in inDict.keys():
        fileLength += 8 + len(inDict[key])
    writeUInt(file,fileLength)
    file.write(b"WAVE")
    for key in inDict.keys():
        if key != b"data":
            file.write(key)
            writeUInt(file,len(inDict[key]))
            file.write(inDict[key])
    key = b"data"
    file.write(key)
    writeUInt(file,len(inDict[key]))
    file.write(inDict[key])

def CopyMetadata(source,mutate):
    assert isinstance(source,BufferedReader)
    assert isinstance(mutate,BufferedReader)
    sourceData = dict()
    mutateData = dict()
    ReadWavIntoDict(source,sourceData)
    ReadWavIntoDict(mutate,mutateData)
    source.close()
    mutate.close()
    #now iterate over keys
    for key in sourceData.keys():
        if key not in mutateData:
            mutateData[key] = sourceData[key]
    WriteWavFromDict(open(mutate.name,'wb'),mutateData)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        CopyMetadata(open(sys.argv[1],'rb'),open(sys.argv[2],'rb'))
    else:
        source = input("Input the filepath to the donor wav:")
        mutate = input("Input the filepath to the wav which is receiving the metadata:")
        CopyMetadata(open(source,'rb'),open(mutate,'rb'))